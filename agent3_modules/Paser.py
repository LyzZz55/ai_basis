
from camel.societies import RolePlaying
from camel.agents import ChatAgent
from camel.utils import print_text_animated
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
import json

import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")


import sys
from pathlib import Path
# 获取项目根目录并添加到sys.path
project_root = str(Path(__file__).parent.parent.parent)  # 根据实际结构调整
sys.path.append(project_root)
# 使用绝对导入
from utils import output

gemini_model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_1_5_FLASH,
    model_config_dict={
        "max_tokens": 8192,
        "temperature": 0.01
    },
    api_key=GEMINI_API_KEY
)
dpskv3_model = ModelFactory.create(
    model_platform=ModelPlatformType.SILICONFLOW,
    model_type='Pro/deepseek-ai/DeepSeek-R1',
    model_config_dict={
        "max_tokens": 8192,
        "temperature": 0.01
    },
    api_key=SF_API_KEY,
)

# 这里写函数，用Agent提取需要的块




# 写函数，提取calendat
calendar_system_message ='''
    你是一个营销任务分析专家，擅长将复杂的营销计划拆分为具体的可执行任务。
    请你将营销计划拆分为具体的任务，每个任务包含：  
    - 任务名称(task_name)
    - 任务描述(task_description)
    - 发布具体实践(time)

    请返回JSON格式的任务列表。最终的输出必须是一个严格的JSON格式对象，不得包含任何JSON格式之外的解释性文字或前言。比如：
{  
  "tasks": [  
    {  
      "task_name": "7月抖音干细胞科普动画制作",  
      "task_description": "制作30秒动画《5步看懂干细胞变护肤品》，配'微囊不是魔法，是慢释放小水弹'标语，植入会员注册入口",  
      "platform": "抖音",  
      "time": "7月2日",  
      "theme": "植物干细胞科普周"  
    },  
    {  
      "task_name": "7月小红书博士IP直播",  
      "task_description": "李媛博士IP直播《从实验室到面膜的成分溯源》，现场演示干细胞萃取实验，发起#成分透明挑战#",  
      "platform": "小红书",  
      "time": "7月3日",  
      "theme": "植物干细胞科普周"  
    },  
    {  
      "task_name": "8月全平台AR碳足迹视频",  
      "task_description": "陈雅开箱视频《一片面膜的碳中和之旅》，演示AR扫描包装显示供应链碳足迹，发起#我的碳积分挑战#",  
      "platform": "全平台",  
      "time": "8月1日",  
      "theme": "AR碳足迹上线周"  
    },  
  ]  
}
'''
# 初始化Agent
task_agent = ChatAgent(
    system_message=calendar_system_message,
    model=dpskv3_model,
    message_window_size=1000,
)

def contents_calendar_to_list(marketing_plan_text)-> dict:
    # 使用Agent分析营销计划  
    output("BLACK", "Start: 分析营销计划", None, False)
    response = task_agent.step(f"""  
    营销计划：  
    {marketing_plan_text}  
    请返回JSON格式的任务列表。  
    """)  
    output("BLACK", "End: 分析营销计划", None, False)
    return json.loads(response.msgs[0].content)

import re
def extract_content_between_delimiters(input_str: str, N: int) -> list[str]:
    """
    提取 report_x_start 到 report_x_end 之间的内容，x 从 1 到 N。
    Args:
        input_str (str): 需要搜索的源字符串。
        N (int): 最大编号。
    Returns:
        list[str]: 所有匹配到的内容列表。
    """
    all_matches = []
    if N < 1:
        return []
    for n in range(1, N + 1):
        # 支持跨多行
        pattern = rf"report_{n}_start(.*?)report_{n}_end"
        matches = re.findall(pattern, input_str, re.DOTALL)
        if matches:
            all_matches.extend([m.strip() for m in matches])
    return all_matches



def process_and_save_delimited_blocks(txt_path: str, N: int, output_dir: str, output_names:list, output_json_name: str = 'agent1_outputs.json'):
    """
    从txt_path读取内容，调用extract_content_between_delimiters，得到list，
    并将每个块分别输出到output_dir下
    """
    if not N == len(output_names):
        output("RED", "process_and_save_delimited_blocks： N与output_names长度不匹配")
        return {}
    # 读取文件内容
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = extract_content_between_delimiters(content, N)
    
    os.makedirs(output_dir, exist_ok=True)
    
    # 依次保存每个块
    output_json = []
    for idx, block in enumerate(blocks):
        out_path = os.path.join(output_dir, output_names[idx] + ".md")
        with open(out_path, 'w', encoding='utf-8') as out_f:
            out_f.write(block.strip())
        output("GREY", f"已输出: {out_path}")
        output_json.append({
            "path": out_path,
            "comment": output_names[idx],
            "type": "text"
        })
    
    output("GREEN", f"{txt_path}已拆分输出为{N}块。名称分别为{output_names}")
    
    json_obj = {"files": output_json}
    json_out_path = os.path.join(output_dir, output_json_name)
    with open(json_out_path, 'w', encoding='utf-8') as jf:
        json.dump(json_obj, jf, ensure_ascii=False, indent=2)
    output("GREEN", f"输出配置文件已生成到：{json_out_path}")


json_out_agent = ChatAgent(
    system_message="请简单地把输入的json字符串用有逻辑的语言输出，不用添加别的信息",
    model=dpskv3_model,
    message_window_size=1000,
)
def JsonToNL(content):
    return json_out_agent.step(f"{content}").msgs[0].content

from typing import Dict, Any
def deal_data_for_agent_3(needed_data_for_agent_three: Dict):
    res = {}
    for key in needed_data_for_agent_three:
        if 'Brand' in key:  # 检查key中是否包含字符'A'
            res["Brand_Social_Media_Strategic_Playbook"] = needed_data_for_agent_three[key]
        elif '_Market' in key:
            res["Comprehensive_Market_And_Competitor_Intelligence_Report"] = needed_data_for_agent_three[key]
        elif 'Idea' in key:
            res["Content_Idea_Repository"] = needed_data_for_agent_three[key]
        elif 'Audience' in key:
            res["Detailed_Target_Audience_Persona_Portfolio"] = needed_data_for_agent_three[key]
    return res
