import os  
import argparse
import sys
import json
from time import time
from dotenv import load_dotenv  
from camel.loaders import create_file_from_raw_bytes  
from colorama import Fore
from termcolor import colored
from camel.societies.workforce import Workforce  
from camel.tasks import Task  
from camel.agents import ChatAgent  
from camel.models import ModelFactory  
from camel.types import ModelPlatformType  
from camel.toolkits import HumanToolkit

from utils import  check_sensitive_word 


def output(color,message,f,std_flag):
    if std_flag:
        print(colored(message,color.lower()))
    if f is not None:
        f.write("--------"+color+"--------\n"
            +message
            +"\n"
        )
    return


def load_file_config(json_path: str) -> dict:  
    """从 JSON 文件加载文件配置"""  
    with open(json_path, 'r', encoding='utf-8') as f:  
        config = json.load(f)  
    return config 

def load_files_from_config(config: dict,f,std_flag) -> dict:  
    """根据配置加载所有文件内容"""  
    file_contents = {}  
      
    for file_info in config.get("files", []):  
        file_path = file_info["path"]  
        comment = file_info.get("comment", "")  
          
        try:  
            with open(file_path, 'rb') as f:  
                file_content = f.read()  
              
            # 使用 CAMEL 的文件处理功能  
            file_obj = create_file_from_raw_bytes(file_content, file_path)  
              
            file_contents[file_path] = {  
                "content": file_obj.docs[0]["page_content"],  
                "comment": comment,  
                "type": file_info.get("type", "unknown")  
            } 
            output("BLACK","\'"+file_path+"\' read",None,True)
        except Exception as e:
            output("BLACK",f"无法加载文件 {file_path}: {e}",None,std_flag)
            return {}
      
    return file_contents

def create_subtask_agents(json_config_path: str, model,f,std_flag):  
    """创建六个子任务代理"""  
    # 加载文件配置和内容  
    config = load_file_config(json_config_path)  
    file_contents = load_files_from_config(config,f,std_flag)
    has_sensitive, words = check_sensitive_word(f"{file_contents}")
    if has_sensitive:
        output("RED", f"发现敏感词：{words}", None, 1)
        exit(1)
    else:
        output("GREY", "没有发现敏感词, going on", None, 1)
        
      
    # 构建文件信息字符串  
    files_info = "\n".join([  
        f"文件: {path}\n注释: {info['comment']}\n类型: {info['type']}\n内容:\n{info['content']}\n---"  
        for path, info in file_contents.items()  
    ])  
      
    # 创建六个专门的子任务代理  
    agents = []  
      
    # 子任务1代理：数据提取和初步分析  
    agent1 = ChatAgent(  
        system_message=f"""你是子任务1专家，负责进行品牌资产数字化与初步分析。  
  
可用文件信息：  
{files_info}  
  
你的职责：  
1. 从提供的文件中提取关键信息和数据  
2. 进行初步的数据整理和分类  
3. 识别重要的模式和趋势  
4. 为后续分析提供清晰的基础  
  
请基于文件内容完成信息提取和初步分析任务。""",  
        model=model  
    )  
      
    # 子任务2代理：深度处理和分析  
    agent2 = ChatAgent(  
        system_message=f"""你是子任务2专家，负责进行全方位竞争对手深度剖析。  
  
可用文件信息：  
{files_info}  
  
你的职责：  
1. 基于子任务1的结果进行深度分析  
2. 运用专业方法处理数据  
3. 发现深层次的洞察和关联  
4. 生成有价值的分析结果  
  
你将接收到子任务1的输出，请结合原始文件进行深度处理。""",  
        model=model  
    )  
      
    # 子任务3代理：综合分析和评估  
    agent3 = ChatAgent(  
        system_message=f"""你是子任务3专家，负责进行行业趋势与社交聆听。  
  
可用文件信息：  
{files_info}  
  
你的职责：  
1. 综合前两个任务的所有结果  
2. 进行跨领域的关联分析  
3. 评估结果的可靠性和有效性  
4. 提供综合性的见解和建议  
  
你将接收到前两个任务的输出，请进行综合分析。""",  
        model=model  
    )  
      
    # 子任务4代理：报告生成和总结  
    agent4 = ChatAgent(  
        system_message=f"""你是子任务4专家，负责进行目标受众360°画像构建。  
  
可用文件信息：  
{files_info}  
  
你的职责：  
1. 整合前三个任务的所有成果  
2. 进行目标受众的画像构建 
3. 分析这个画像构建的可信度
4. 提供综合性的见解和建议  
  
你将接收到前三个任务的输出，请进行画像构建。""",  
        model=model  
    )  
    # 子任务5代理：报告生成和总结
    agent5 = ChatAgent(  
        system_message=f"""你是子任务5专家，负责进行品牌差异化定位与沟通策略制定。  
  
可用文件信息：  
{files_info}  
  
你的职责：  
1. 综合前四个任务的所有结果  
2. 完成品牌差异化定位与沟通策略制定
3. 评估结果的可靠性和有效性  
4. 提供综合性的见解和建议  
  
你将接收到前四个任务的输出，请进行综合分析。""",  
        model=model  
    )  
      
    # 子任务5代理：报告生成和总结  
    agent6 = ChatAgent(  
        system_message=f"""你是子任务6专家，负责生成结构化的最终报告。  
  
可用文件信息：  
{files_info}  
  
你的职责：  
1. 整合前五个任务的所有成果  
2. 严格按照要求的内容生成结构化的最终报告  
3. 确保报告的完整性和逻辑性  
4. 提供清晰的结论和建议  
  
你将接收到前五个任务的输出，请完成报告生成。
请注意，前五个子任务的输出不会提供给用户，只有你生成的报告会被提供。所以对于所有必须的信息，请务必在你的报告中重新输出一次，即使是从前面回答中原样复制。
""",  
        model=model  
    )  
    
    agents = [agent1, agent2, agent3, agent4, agent5, agent6]  
    return agents, files_info


def execute_subtasks_automatically(agents, main_task_content,f,std_flag):  
    """自动执行六个子任务，无人类干预"""  
      
    subtask_descriptions = [  
        """
        子任务1：  品牌资产数字化与初步分析 (Brand Asset Digitization & Initial Analysis):
        1) 抓取并解析品牌官网、现有社交媒体内容，提取当前品牌信息传递、内容主题、互动数据、粉丝评论情感。
        2) 对提供的品牌VI、故事等文档进行NLP分析，提炼核心品牌关键词和价值主张。
        3) 初步评估品牌当前在线声量和情感倾向。
        """,  

        """
        子任务2：全方位竞争对手深度剖析 (Comprehensive Competitor Deep-Dive):
        1)智能识别补充: 基于用户提供的列表和行业信息，通过市场分析工具智能识别另外3-5个潜在或间接竞争对手。
        2)多维度数据采集： 对每个选定的竞争对手（共6-10个）：
            a) 社交媒体表现： 活跃平台、粉丝规模与增长率、发帖频率、内容类型分布（图文/视频/直播/互动）、平均互动率 (点赞、评论、分享)、热门帖子分析。
            b) 内容策略逆向工程： 分析其内容主题、叙事角度、视觉风格、文案语调、常用的#标签、主要营销活动类型。
            c) 受众画像与情感： 分析其粉丝评论、提及品牌的UGC，推断其受众特征及对该品牌的情感。
            d) 广告投放情况 (可选，若工具支持)： 预估其在社交媒体的广告投放策略和创意。
            e) 网站流量与SEO策略 (可选)： 简要分析其网站流量来源及主要关键词排名，以了解其整体数字营销协同性。
        3) 生成竞品对比矩阵： 清晰展示各竞品在关键维度上的表现和策略差异。
        """,   

        """
        子任务3：行业趋势与社交聆听 (Industry Trends & Social Listening):
        1) 宏观趋势： 分析所在行业的最新市场报告、权威媒体资讯，识别宏观发展趋势、新兴技术/概念。
        2) 社交热点与话题追踪： 利用社交聆听工具，实时监测与品牌行业、产品、目标受众相关的热门话题、病毒内容、网络迷因 (Memes)、挑战赛等。
        3) 关键词与#标签生态分析： 识别行业核心关键词、长尾关键词、以及各类平台上的热门/潜力#标签簇。
        4) KOL/KOC识别与分析： 找出行业内有影响力的意见领袖 (KOL) 和关键意见消费者 (KOC)，分析其内容特点、粉丝画像、合作品牌。
        """,  

        """
        子任务4：目标受众360°画像构建 (360° Target Audience Persona Development):
        1) 数据融合： 整合品牌方提供的初步画像、竞品受众分析、行业社交聆听数据。
        2) 多维细化： 构建2-4个高度具体的目标受众画像 (Personas)，每个画像包含：
            a) 基本人口统计学： 姓名（虚拟）、年龄、性别、地理位置、职业、收入水平、教育背景、家庭状况。
            b)生活方式与价值观： 兴趣爱好、日常习惯、消费观念、关注的社会议题、生活目标与追求。
            c) 数字行为特征： 常用的社交媒体平台、活跃时段、内容偏好（图文/短视频/直播/深度文章）、信息获取渠道、信任的KOL/KOC。
            d) 痛点与需求： 与品牌产品/服务相关的未被满足的需求、使用现有解决方案的痛点。
            e) 购买决策驱动因素： 影响其购买决策的关键因素（价格、品牌、口碑、功能、情感连接等）。
            f) 品牌互动偏好： 期望与品牌建立怎样的关系，喜欢怎样的互动方式。
        3) 用户旅程初步映射： 针对每个Persona，初步勾勒其在认知、兴趣、考虑、购买、忠诚等阶段的行为特征和信息需求。
        """,

        """
        子任务5：品牌差异化定位与沟通策略制定 (Brand Differentiation & Communication Strategy Formulation):
        1) SWOT分析与机会识别： 结合内外部环境分析，明确品牌的核心优势、劣势、市场机会与潜在威胁。
        2) 独特销售主张 (USP) 精炼： 在市场竞争格局和目标受众需求的基础上，打磨或重塑品牌/产品的核心USP。
        3) 品牌“人设”与“语调”定义： 为品牌在社交媒体上设定一个鲜明、一致且吸引目标受众的“人格化形象”（如：智慧导师型、幽默玩伴型、精致生活家型）和相应的沟通语调（如：专业严谨、亲切活泼、犀利风趣、温暖治愈）。
        4) 核心信息屋 (Message House) 构建： 围绕USP和品牌人设，构建包含1个核心信息、3-4个支持性信息支柱和相应证据/例证的核心信息架构。
        5) 平台选择与角色分配： 根据目标受众画像的平台偏好、各平台特性及营销目标，推荐2-3个核心运营的社交媒体平台，并明确每个平台在整体营销策略中扮演的角色和侧重的内容方向（例如：微信公众号做深度内容沉淀和用户服务，微博做热点追踪和即时互动，小红书做生活方式种草和UGC激励，抖音做短平快趣味科普和品牌形象展示）。
        """,

        """
        子任务6：结构化信息整理：
        1) `Comprehensive_Market_And_Competitor_Intelligence_Report`:
            a) 第一部分：品牌现状评估 (Brand Current State Assessment): 包括在线声量、情感概览、现有内容资产分析。
            b) 第二部分：深度竞争格局分析 (In-depth Competitive Landscape Analysis): 每个核心竞品的详细档案（社交表现、内容策略、视觉风格、受众反馈等），以及横向对比矩阵图。
            c) 第三部分：行业趋势与机会洞察 (Industry Trends & Opportunity Insights): 当前及未来1-2年行业内容趋势、热门话题和技术应用、KOL/KOC生态图谱。
        2) `Detailed_Target_Audience_Persona_Portfolio`: 2-4个图文并茂的目标受众画像，包含所有细化维度，并附带每个Persona的典型用户旅程地图（AIDA或类似模型）。
        3) `Brand_Social_Media_Strategic_Playbook`:
            a) 核心定位： 精炼后的USP、品牌社交媒体“人设”定义及阐释、沟通“语调”指南（含示例）。
            b) 信息架构： 核心信息屋 (Message House) 详情。
            c) 平台战略： 推荐的核心社交媒体平台组合，各平台在营销矩阵中的角色定位、核心目标和内容方向。
            d) 初步KPI框架： 建议与营销目标和平台角色挂钩的初步关键绩效指标 (KPIs) 类型。
        请在输出这三个报告时分别在头部和尾部加上标识符"report_x_start","report_x_end",其中x为阿拉伯数字1,2,3等
        请严格遵循系统提示词，完成系统提示词给明的任务
        """
    ]  
      
    task_results = []  
    output("GREY","=== 开始自动执行六个子任务 ===\n",f,std_flag)
      
    for i, (agent, description) in enumerate(zip(agents, subtask_descriptions)):
        output("GREY",f"执行 {description}",f,std_flag)
          
        # 构建任务提示  
        task_prompt = f"""  
请执行以下任务：{description}  
  
原始任务：{main_task_content}  
  
前序任务结果：  
{chr(10).join([f"任务{j+1}结果: {result}" for j, result in enumerate(task_results)])}  
  
请基于已提供的文件信息和前序任务结果完成这个子任务。  
"""  
          
        # 执行任务  
        start_time=time()
        response = agent.step(task_prompt)  
        result = response.msgs[0].content  
        task_results.append(result)  
        output("GREY",f"✓ 子任务 {i+1} 完成\n",f,std_flag) 
        end_time=time()
        output("RED","time cost: %d"%(end_time-start_time),f,std_flag)
      
    # 整合所有结果生成基础回答  
    base_answer = f""" 
前5个子任务的分析结果如下：
  
## 子任务1  
{task_results[0]}  
  
## 子任务2    
{task_results[1]}  
  
## 子任务3  
{task_results[2]}  
  
## 子任务4  
{task_results[3]}  

## 子任务5 
{task_results[4]}  

基于前5个子任务的回答，子任务6生成出的最终报告如下：

## 子任务6:最终报告
{task_results[5]}  
 
"""  
    output("GREY","=== 六个子任务自动执行完成 ===",f,std_flag)
    output("GREY","生成的基础回答：",f,std_flag)
    output("GREY",base_answer,f,std_flag)
      
    return base_answer, task_results


def create_improvement_agent(model, base_answer, task_results, files_info,f,std_flag):  
    """创建用于与人类交互改进回答的代理"""  
      
    # 构建包含所有上下文的系统消息  
    system_message = f"""你是一个专业的回答改进专家，负责与人类协作不断优化和改进回答质量。  
  
你已经获得了一个基础回答和详细的分析过程：  
  
=== 基础回答 ===  
{base_answer}  
  
=== 详细的子任务结果 ===  
子任务1结果：{task_results[0]}  
  
子任务2结果：{task_results[1]}  
  
子任务3结果：{task_results[2]}  
  
子任务4结果：{task_results[3]}  

子任务5结果：{task_results[4]} 

子任务6结果，即最终输出的报告：{task_results[5]} 
  
=== 原始文件信息 ===  
{files_info}  
  
你的职责：  
1. 理解人类的反馈和改进建议  
2. 基于反馈对回答进行针对性的改进  
3. 保持回答的准确性和完整性  
4. 与人类进行有效的沟通和协作  
5. 不断迭代直到人类满意  
  
请根据人类的指导来改进回答，确保最终结果符合人类的期望和要求。、
请牢记，你只需要对子任务6的结果，即最终输出的报告按照人类的要求进行修改即可，输出时也无需重复输出前五个子任务的结果。
"""  
      
    # 创建带有人类交互工具的代理  
    human_toolkit = HumanToolkit()  
      
    agent = ChatAgent(  
        system_message=system_message,  
        model=model,  
        tools=[*human_toolkit.get_tools()]  
    )  
      
    return agent

def improve_answer_with_human_interaction(improvement_agent, base_answer,task_results,f,std_flag):  
    """与人类交互改进回答"""  
      
    current_answer = base_answer  
    iteration = 0  
    output("GREY","\n=== 开始人类交互改进阶段 ===",f,std_flag)
    for i in range(5):
        output("GREY","子任务 %d 回答："%(i+1),f,std_flag)
        col="BLUE" if i%2==0 else "GREEN"
        output(col,task_results[i],f,std_flag)

    output("GREY","当前子任务6生成报告：",f,std_flag)
    output("CYAN",task_results[5],f,std_flag)

    flag=True
    while True:  
        iteration += 1 
        output("GREY",f"\n--- 改进轮次 {iteration} ---",f,std_flag)
          
        # 获取人类反馈
        while True:
            need_to_modify=input("\n请问是否满意？(y/n):").lower()
            if need_to_modify in ['y','n','yes','no']:
                break
        if need_to_modify in ['y','yes']:
            output("GREEN","✓ 人类确认满意，改进完成！",f,std_flag)
            break


        while True:
            human_feedback=input("\n请输入您的反馈和改进建议(输入'q'/'quit'退出)：")
            if human_feedback.strip():
                break
        if human_feedback.lower() in ['q','quit']:
            output("RED","× 退出改进流程",f,std_flag)
            break

          
        # 构建改进提示  
        improvement_prompt = f"""  
当前回答：  
{current_answer}  
  
人类反馈：  
{human_feedback}  
  
请根据人类的反馈对当前回答进行改进。保持回答的准确性和完整性，同时满足人类的具体要求。  
你只需要生成修改后的报告，即你只需要按照人类要求在子任务六的回答基础上进行修改或添加。
前五个子任务的回答仅作为提示给出，你的回答中无需包含！！！
"""  
          
        # 代理处理改进请求  
        response = improvement_agent.step(improvement_prompt)  
        improved_answer = response.msgs[0].content  
        output("GREY",f"\n改进后的回答：",f,std_flag)
        output("CYAN",improved_answer,f,std_flag)
          
        # 更新当前回答  
        current_answer = improved_answer
        flag=False
          
        # 询问是否需要进一步改进  
        continue_improvement = input("\n是否需要进一步改进？(y/n): ")  
        if continue_improvement.lower() not in ['y', 'yes', '是', '需要']:
            output("GREEN","✓ 改进完成！",f,std_flag)
            break  
    
    if flag:
        current_answer=task_results[5]
    return current_answer

def main(args):
    if args.input is None:
        print("No input file")
        return
    if args.output is None:
        print("No output file")
        return
    
    if args.log is not None:
        f=open(args.log,'w',encoding="utf-8",buffering=1)
    else:
        f=None
    load_dotenv(dotenv_path='.env')
    api_key = os.getenv('SILICONFLOW_API_KEY')
    output("BLACK","SILICONFLOW_API_KEY:%s"%(api_key),None,True)

    model = ModelFactory.create(  
        model_platform=ModelPlatformType.SILICONFLOW,  
        model_type="deepseek-ai/DeepSeek-R1", 
        api_key=api_key,
        model_config_dict={
            "temperature":0.7
        },
        timeout=1800
    )
    output("BLACK","model initialized",None,True)

    main_task = "基于提供的文件进行全面的品牌分析，包括数据提取、处理、分析和报告生成" 

    output("GREY","=== 开始两阶段任务处理流程 ===",f,args.std_flag)
      
    # 阶段1：创建子任务代理并自动执行
    output("GREY","\n阶段1：自动执行六个子任务",f,args.std_flag)

    subtask_agents, files_info = create_subtask_agents(args.input, model,f,args.std_flag)  
    base_answer, task_results = execute_subtasks_automatically(subtask_agents, main_task,f,args.std_flag)  
      
    # 阶段2：创建改进代理并与人类交互  
    output("GREY","\n阶段2：人类交互改进",f,args.std_flag)

    improvement_agent = create_improvement_agent(model, base_answer, task_results, files_info,f,args.std_flag)  
    final_answer = improve_answer_with_human_interaction(improvement_agent, base_answer,task_results,f,args.std_flag)  
      
    output("GREY","\n=== 最终结果 ===",f,args.std_flag) 
    output("CYAN",final_answer,f,args.std_flag)
      
    # 保存结果  
    with open(args.output, "w", encoding="utf-8",buffering=1) as outf:  
        outf.write("=== 最终结果 ===\n")  
        outf.write(final_answer)  
    output("GREY","\n结果已保存到 "+args.output,f,args.std_flag)
    if f is not None:
        f.close()
    return

