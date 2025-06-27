import json
import os
import re
import traceback
from typing import List, Dict, Any

import pandas as pd
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.types import RoleType

# utils: 读取Agent1输出部分的组件,为了避免主文件太乱了我就分立了一个文件
import utils

# 用于读取api,我将自己的api放在了同目录下的key文件中,联合使用的时候api可以换成老师给的公用的api,基于SiliconFlow平台
try:
    from key import key
except ImportError:
    print("错误：无法从 key.py 导入 API 密钥。")
    print("请创建一个名为 key.py 的文件，并在其中定义变量: key = '您的SiliconFlow_API密钥'")
    exit()


class ContentCreativityAgent:
    """
    Agent 2: 内容创意孵化与多维形式策划 Agent主类
    """

    def __init__(self, model, input_json_path: str):
        self.model = model
        config = utils.load_file_config(input_json_path)
        self.input_data = utils.load_files_from_config(config)
        if not self.input_data:
            raise ValueError("输入数据加载失败，无法初始化 Agent。")
        self.output_files = []

    def _format_inputs_for_prompt(self) -> str:
        """将加载的输入数据格式化为字符串，以便注入到Prompt中。"""
        formatted_string = ""
        for comment, data in self.input_data.items():
            formatted_string += f"--- {comment} ---\n"
            formatted_string += f"{data['content']}\n\n"
        return formatted_string

    def _execute_prompt(self, prompt: str) -> str:
        print("🤖 向LLM发送请求... (Sending request to LLM...)")
        system_message_obj = BaseMessage(
            role_name="内容策略与创意专家 (Content Strategy and Creative Expert)",
            role_type=RoleType.ASSISTANT,
            meta_dict=None,
            content="你是一位世界顶级的社交媒体内容策略师和创意总监，专注于为品牌创造有吸引力、有策略、可执行的内容计划。"
                    "你会根据提供的品牌战略、用户画像和营销目标，系统性地进行构思和规划。请严格按照用户的指令格式输出内容。"
        )
        agent = ChatAgent(system_message=system_message_obj, model=self.model, output_language="zh")
        user_message_obj = BaseMessage(
            role_name="市场部经理 (Marketing Manager)",
            role_type=RoleType.USER,
            meta_dict=None,
            content=prompt
        )
        try:
            response = agent.step(user_message_obj)
            if response.msgs is None or not response.msgs:
                print("❌ LLM响应为空。(LLM response is empty.)")
                return "LLM未能生成响应。"
            llm_output = response.msgs[0].content
            for chunk in response:  
                if hasattr(chunk, 'content') and chunk.content:  
                    print(chunk.content, end='', flush=True)
            print("✅ LLM响应接收完毕。(LLM response received.)")
            return llm_output
        except Exception as e:
            print(f"❌ 调用LLM时发生错误 (An error occurred while calling LLM): {e}")
            traceback.print_exc()
            return f"调用API时出错: {e}"

    def _real_seo_tool_with_llm(self, topic: str, num_keywords: int = 8) -> List[str]:
        """利用 LLM API 动态生成 SEO 关键词的真实工具函数。"""
        print(f"正在通过 LLM 为 '{topic}' 查询关键词...")
        seo_prompt = f"""
        你是一名顶级的SEO（搜索引擎优化）专家。你的任务是为一个给定的内容主题生成一系列高度相关、具有潜在搜索流量的关键词。
        请遵循以下规则：
        1.  分析主题的核心概念和目标受众。
        2.  生成 {num_keywords} 个关键词，包括核心关键词、长尾关键词和相关问题式关键词。
        3.  不要添加任何解释、标题或介绍。
        4.  只返回关键词本身，每个关键词占一行。
        内容主题是：
        "{topic}"
        请严格遵循规则，完成给明的任务
        
        """
        try:
            response = self._execute_prompt(seo_prompt)
            keywords = [line.strip() for line in response.strip().split('\n') if line.strip()]
            cleaned_keywords = [re.sub(r'^\s*\d+\.\s*|\s*-\s*', '', kw) for kw in keywords if kw]
            if not cleaned_keywords:
                print("  > WARN [SEO Tool]: LLM 返回为空或无法解析，将返回空列表。")
                return []
            print(f"  > 生成的关键词: {cleaned_keywords}")
            return cleaned_keywords
        except Exception as e:
            print(f"  > ERROR [SEO Tool]: 调用 LLM 生成关键词时发生错误: {e}")
            return []

    def _mock_push_to_trello(self, calendar_df: pd.DataFrame):
        print("\n 正在将内容日历同步到Trello...")
        print(f"  > 成功创建了 {len(calendar_df)} 张卡片到一个新的 '内容日历' 看板。")
        return {"status": "success", "board_url": "https://trello.com/b/mock_board_link"}

    def run_ideation_and_filtering(self) -> List[Dict[str, Any]]:
        print("\n===== 任务1: 开始多维度创意风暴与筛选 =====")
        formatted_inputs = self._format_inputs_for_prompt()
        prompt = f"""
        **核心任务: 创意风暴与初步筛选**
        **输入信息 (来自Agent 1):**
        {formatted_inputs}
        **你的工作:**
        1.  **发散构思**: 根据上述所有输入信息，进行大量创意构思。
        2.  **初步筛选与打分**: 从你的海量构思中，筛选出10个最优质的创意点。
        3.  **输出格式**: 请严格按照以下格式，以Markdown表格形式返回这10个创意点，不要有任何解释或开场白。
        | Idea_ID | Creative_Title | Target_Persona | Core_Pillar | Brief_Description | Potential_Formats | Score_Brand_Fit (1-10) | Score_Audience_Attraction (1-10) | Score_Feasibility (1-10) |
        |---|---|---|---|---|---|---|---|---|
        请严格遵循规则，完成给明的任务
        """
        response = self._execute_prompt(prompt)
        try:
            lines = [line for line in response.strip().split('\n') if '|' in line and '---' not in line]
            if not lines: raise ValueError("No table data found")
            headers = [h.strip() for h in lines[0].strip('|').split('|')]
            data = [dict(zip(headers, [v.strip() for v in line.strip('|').split('|')])) for line in lines[1:]]
            print("✅ 创意风暴表格解析成功。")
            return data
        except Exception as e:
            print(f"❌ 解析创意风暴Markdown表格失败: {e}\n原始回应:\n{response}")
            return [{"raw_response": response}]

    def plan_content_series(self, ideas: List[Dict[str, Any]]) -> str:
        print("\n===== 任务2: 开始内容主题与系列规划 =====")
        ideas_str = "\n".join([f"- {i.get('Creative_Title', '')}: {i.get('Brief_Description', '')}" for i in ideas])
        # 【补全】plan_content_series 的 prompt
        prompt = f"""
        **核心任务: 内容主题系列规划**
        **背景信息:**
        我正在为一个品牌进行内容规划，已经有了一批初步筛选过的创意点。
        **输入信息:**
        - **已筛选的优质创意点列表**: 
          {ideas_str}
        - **品牌战略核心信息支柱**: (请根据Agent 1的输入自行提炼，例如：营养科学, 都市生活方式, 可持续性与来源, 社区与互动)
        **你的工作:**
        1. 将上述创意点进行归类和提炼。
        2. 围绕品牌的核心信息支柱，规划出3-4个可持续的内容主题系列（或称内容栏目）。
        3. 为每个系列提供清晰的定位、目标受众细分、核心价值和建议的更新频次。
        **输出格式**: 请严格按照以下Markdown格式输出，不要包含任何解释或开场白。
        ### 内容系列1: [系列名称]
        - **定位**: [这个系列的独特价值和风格]
        - **目标受众细分**: [主要针对哪个或哪些用户画像]
        - **核心价值传递**: [这个系列主要传递品牌什么信息]
        - **大致更新频次建议**: [例如: 每周一期]
        - **包含的创意示例**:
            - [相关创意标题1]
            - [相关创意标题2]

        ### 内容系列2: [系列名称]
        - **定位**: ...
        请严格遵循规则，完成核心任务
        """
        response = self._execute_prompt(prompt)
        file_path = "outputs/Detailed_Content_Series_Blueprints.txt"
        with open(file_path, "w", encoding="utf-8") as f: f.write(response)
        print(f"✅ 内容系列规划已生成并保存到 '{file_path}'")
        self.output_files.append({"path": file_path, "comment": "内容主题系列的详细规划蓝图", "type": "text"})
        return response

    def refine_formats_and_platforms(self, top_idea: Dict[str, Any]) -> str:
        print("\n===== 任务3: 开始内容形式与平台适配 (一鱼多吃) =====")
        # 【补全】refine_formats_and_platforms 的 prompt
        prompt = f"""
        **核心任务: "一鱼多吃"跨平台分发策略规划**
        **核心内容创意:**
        - **标题**: {top_idea.get('Creative_Title')}
        - **描述**: {top_idea.get('Brief_Description')}
        - **主要形式建议**: {top_idea.get('Potential_Formats')}
        **你的工作:**
        假设上述核心内容将被制作成其主要形式（例如一篇深度图文报告或一个核心Vlog），请为其规划一个详细的跨平台分发和再创作策略。
        **目标平台**: 微信公众号, 微博, 抖音, 小红书, B站
        **输出格式**: 请为每个平台提供具体的执行建议，包括内容形式、优化重点和CTA（Call to Action）。严格按照下面的格式输出，不要有任何额外说明。
        ## 核心内容: "{top_idea.get('Creative_Title')}" - 跨平台分发指南
        ### 1. 微信公众号
        - **内容形式**: 
        - **优化重点**: 
        - **CTA (Call to Action)**: 
        ### 2. 微博
        - **内容形式**: 
        - **优化重点**: 
        - **CTA (Call to Action)**: 
        ### 3. 抖音/快手
        - **内容形式**: 
        - **优化重点**: 
        - **CTA (Call to Action)**: 
        ### 4. 小红书
        - **内容形式**: 
        - **优化重点**: 
        - **CTA (Call to Action)**: 
        ### 5. B站
        - **内容形式**: 
        - **优化重点**: 
        - **CTA (Call to Action)**: 
        请严格遵循规则，完成核心任务
        """
        response = self._execute_prompt(prompt)
        file_path = "outputs/Cross-Platform_Content_Repurposing_Guide.txt"
        with open(file_path, "w", encoding="utf-8") as f: f.write(response)
        print(f"✅ 跨平台分发指南已生成并保存到 '{file_path}'")
        self.output_files.append({"path": file_path, "comment": "旗舰内容的“一鱼多吃”跨平台分发指南", "type": "text"})
        return response

    def develop_flagship_content(self, idea: Dict[str, Any]) -> str:
        print("\n===== 任务4: 开始旗舰内容深度策划 =====")
        creative_title = idea.get('Creative_Title', 'Untitled')
        seo_keywords = self._real_seo_tool_with_llm(creative_title)
        # 【补全】develop_flagship_content 的 prompt
        prompt = f"""
        **核心任务: 旗舰级内容深度策划**
        **策划对象:**
        - **创意标题**: {creative_title}
        - **简要描述**: {idea.get('Brief_Description')}
        **你的工作:**
        假设这是一个图文类旗舰内容（例如微信长文或博客文章），请为其撰写一个详细的策划大纲。
        **要求:**
        - 包含清晰的层级结构（H1, H2, H3）。
        - 提出核心论点和数据/案例支撑点。
        - 规划图表或图片的位置和内容。
        - 设计一个引人入胜的开头和强有力的结尾，包含明确的CTA。
        - **请在内容中，自然地融入以下SEO关键词。**
        **相关SEO关键词 (请在内容中合理使用)**: {', '.join(seo_keywords)}
        **输出格式**: 请以Markdown格式输出详细大纲，不要包含任何解释或开场白。
        # H1: [文章主标题，必须吸引人]
        ## 引言 (Introduction)
        [在这里写引人入胜的开头，提出核心问题或痛点]
        ## H2: [第一个主要部分]
        ### H3: [第一个子论点]
        [阐述论点，并指出需要的数据或案例支撑]
        - **图表规划**: [例如：此处插入一个成分对比图]
        ### H3: [第二个子论点]
        ...
        ## H2: [第二个主要部分]
        ...
        ## 结论 (Conclusion)
        [总结全文，并给出强有力的结尾]
        - **CTA (Call to Action)**: [例如：立即访问官网，了解更多产品详情！]
        请生成的内容不需要```md ```等类似的包围，直接生成所需内容
        请严格遵循规则，完成核心任务
        """
        response = self._execute_prompt(prompt)
        sanitized_title = re.sub(r'[\\/*?:"<>|]', "", creative_title)
        safe_filename_part = sanitized_title.strip().replace(' ', '_')
        file_path = f"outputs/Flagship_Brief_{idea.get('Idea_ID', 'X')}_{safe_filename_part}.txt"
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response)
            print(f"✅ 旗舰内容策划案已生成并保存到 '{file_path}'")
            self.output_files.append(
                {"path": file_path, "comment": f"旗舰内容 '{creative_title}' 的深度策划案/大纲", "type": "text"})
        except OSError as e:
            print(f"❌ 保存文件时发生错误: {e}")
        return response

    def draft_ab_test_copy(self, idea: Dict[str, Any]) -> str:
        print("\n===== 任务5: 开始撰写A/B测试文案 =====")
        prompt = f"""
        **核心任务: 为社交媒体帖子撰写A/B测试文案**
        **内容创意:**
        - **标题**: {idea.get('Creative_Title')}
        - **平台**: 微博
        **你的工作:**
        请为这个创意撰写两种不同风格的微博文案初稿（A版和B版），用于A/B测试。
        - **A版**: 采用更**感性、故事化**的语调，与用户建立情感连接。可以讲一个用户的小故事或描绘一个场景。
        - **B版**: 采用更**理性、干货**的语调，突出产品的具体卖点和数据。直接给出核心价值和利益点。
        **要求:**
        - 每版文案包含标题、正文、标签和CTA。
        - 文案长度适合微博平台（140字以内为佳）。
        - 设计一个简单的衡量指标建议。
        **输出格式**: 请严格按照以下格式输出，不要有任何额外说明。
        ## 微博文案A/B测试方案: {idea.get('Creative_Title')}
        ### A版 (感性故事)
        - **标题**: 
        - **正文**: 
        - **标签**: #...
        - **CTA**: 
        ### B版 (理性干货)
        - **标题**: 
        - **正文**: 
        - **标签**: #...
        - **CTA**: 
        ### 测试衡量建议
        - **主要指标**: [例如：点击率 (CTR) 或 互动率 (Engagement Rate)]
        - **观察周期**: [例如：发布后24小时]
        请严格遵循规则，完成核心任务
        """
        response = self._execute_prompt(prompt)
        file_path = "outputs/Draft_Copy_AB_Testing_Proposals.txt"
        with open(file_path, "w", encoding="utf-8") as f: f.write(response)
        print(f"✅ A/B测试文案已生成并保存到 '{file_path}'")
        self.output_files.append({"path": file_path, "comment": "社交媒体帖子的A/B测试文案初稿", "type": "text"})
        return response

    def create_editorial_calendar(self, ideas: List[Dict[str, Any]]) -> pd.DataFrame:
        """6. 内容日历精细化编排"""
        print("\n===== 任务6: 开始创建内容日历 =====")
        ideas_str = "\n".join([f"- {i.get('Creative_Title')}" for i in ideas])
        context_inputs = self._format_inputs_for_prompt()
        prompt = f"""
        **核心任务: 创建未来一个月的内容日历**
        **背景信息 (Context):**
        {context_inputs}
        **输入信息 (Inputs):**
        - **创意列表**: 
          {ideas_str}
        - **用户活跃时间**: 工作日午休 (12:00-13:30), 晚间 (20:00-23:00); 周末下午和晚上。
        - **内容配比原则**: 请遵循 80/20 法则（80%价值内容，20%促销内容），并确保信息性、娱乐性、互动性内容的平衡。
        **你的工作:**
        请为接下来的4周（从下周一开始）创建一个详细的内容日历。在日历中合理安排上述创意，并补充一些日常互动型内容（如提问、投票）。
        **输出格式**: 请严格以Markdown表格输出，不要包含任何解释或开场白。列名和顺序必须如下所示。请至少生成10-15条内容项。
        | Publish_Date | Publish_Time | Target_Platform | Content_Series | Content_Title | Main_Format | CTA | Notes |
        |---|---|---|---|---|---|---|---|
        请严格遵循规则，完成核心任务
        """
        response = self._execute_prompt(prompt)
        try:
            lines = [line for line in response.strip().split('\n') if '|' in line and '---' not in line]
            if not lines:
                print(f"❌ 解析内容日历Markdown表格失败: No table data found in the response.")
                print("---------- LLM 原始回应 (Raw Response) ----------")
                print(response)
                print("-------------------------------------------------")
                raise ValueError("No table data found")
            headers = [h.strip() for h in lines[0].strip('|').split('|')]
            data_rows = [[v.strip() for v in line.strip('|').split('|')] for line in lines[1:] if
                         len(line.strip('|').split('|')) == len(headers)]
            df = pd.DataFrame(data_rows, columns=headers)
            file_path = "outputs/Master_Editorial_Calendar.xlsx"
            df.to_excel(file_path, index=False)
            print(f"✅ 内容日历已成功生成并保存为 '{file_path}'")
            self.output_files.append({"path": file_path, "comment": "未来1-3个月的精细化内容日历", "type": "excel"})
            return df
        except Exception as e:
            print(f"❌ 在处理日历回应时发生错误: {e}")
            return pd.DataFrame()

    def _write_output_json(self, output_json_path: str):
        """将所有输出文件的信息写入一个JSON配置文件。"""
        print(f"\n正在生成 Agent 2 的输出配置文件到 '{output_json_path}'...")
        output_config = {"files": self.output_files}
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(output_config, f, ensure_ascii=False, indent=4)
        print("✅ 输出配置文件生成完毕！")

    def execute_planning_flow(self):
        """Executes the complete planning workflow."""
        if not os.path.exists("outputs"): os.makedirs("outputs")
        ideas = self.run_ideation_and_filtering()
        if not ideas or "raw_response" in ideas[0]:
            print("创意生成失败，流程终止。")
            return
        idea_repo_path = "outputs/Content_Idea_Repository.xlsx"
        pd.DataFrame(ideas).to_excel(idea_repo_path, index=False)
        print(f"✅ 创意库已保存到 '{idea_repo_path}'")
        self.output_files.append({"path": idea_repo_path, "comment": "内容创意库及优先级排序矩阵", "type": "excel"})
        self.plan_content_series(ideas)
        if ideas:
            flagship_idea = ideas[0]
            self.refine_formats_and_platforms(flagship_idea)
            self.develop_flagship_content(flagship_idea)
            self.draft_ab_test_copy(flagship_idea)
        calendar_df = self.create_editorial_calendar(ideas)
        if not calendar_df.empty: self._mock_push_to_trello(calendar_df)
        self._write_output_json("outputs/agent2_outputs.json")
        print("\n🎉🎉🎉 Agent 2 内容创意策划流程全部完成！ 🎉🎉🎉")
        print("所有输出文件均已保存在 'outputs' 文件夹下。")


def main(input_config_path: str):
    SILICONFLOW_API_URL = "https://api.siliconflow.cn/v1"
    SILICONFLOW_MODEL_NAME = "deepseek-ai/DeepSeek-V3"  # 我自己的api最高能使用的模型就是V3,如果老师分发的API能使用更先进的模型,可以后续进行更改,但必须保证模型可调用.
    print(f"正在初始化模型 (Initializing model): {SILICONFLOW_MODEL_NAME}")
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
        model_type=SILICONFLOW_MODEL_NAME,
        url=SILICONFLOW_API_URL,
        api_key=key,
        model_config_dict={"stream": True, "temperature": 0.75, "max_tokens": 4096, "timeout": 120}
        # 这里temperature可以随意调节,我尝试了0.5-1.2, 停留在0.75, 事实上0.7也是一个不错的选择
    )

    # --- Agent 实例化与执行 ---
    input_config_path
    try:
        content_agent = ContentCreativityAgent(model, input_config_path)
        content_agent.execute_planning_flow()
    except (FileNotFoundError, ValueError) as e:
        print(f"\n❌ 启动失败: {e}")
        print(f"请确保 '{input_config_path}' 文件存在，并且其指向的所有文件路径都正确。")
