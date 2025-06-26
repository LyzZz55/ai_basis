
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
from part_3.utils import output

gemini_model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_1_5_FLASH,
    model_config_dict={
        "max_tokens": 8192,
        "temperature": 0.7
    },
    api_key=GEMINI_API_KEY
)
dpskv3_model = ModelFactory.create(
    model_platform=ModelPlatformType.SILICONFLOW,
    model_type='Pro/deepseek-ai/DeepSeek-R1',
    model_config_dict={
        "max_tokens": 8192,
        "temperature": 0.7
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

def contents_calendar_to_list(marketing_plan_text: str)-> dict:
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
import re

def extract_custom_content(
    input_str: str, 
    N: int, 
    start_prefix: str, 
    start_suffix: str, 
    end_prefix: str, 
    end_suffix: str
) -> list[str]:
    """
    在一个字符串中，根据用户自定义的复杂标记和数字 N，提取它们之间的内容。
    
    此函数能处理内容与标记之间的换行符。

    Args:
        input_str (str): 需要搜索的源字符串。
        N (int): 一个正整数，定义了分隔符中数字 n 的最大值 (n 从 1 到 N)。
        start_prefix (str): 开始标记中，数字 n 前面的部分 (例如 'xxxx')。
        start_suffix (str): 开始标记中，数字 n 后面的部分 (例如 'xxx')。
        end_prefix (str): 结束标记中，数字 n 前面的部分 (例如 'yyyy')。
        end_suffix (str): 结束标记中，数字 n 后面的部分 (例如 'yyy')。

    Returns:
        list[str]: 一个包含所有匹配到的、并清除了首尾空白的字符串列表。
    """
    all_matches = []
    if N < 1:
        return []

    # 为了安全起见，对用户输入的标记部分进行转义，防止它们包含特殊的正则表达式字符（如 . * + ? 等）
    esc_start_prefix = re.escape(start_prefix)
    esc_start_suffix = re.escape(start_suffix)
    esc_end_prefix = re.escape(end_prefix)
    esc_end_suffix = re.escape(end_suffix)

    for n in range(1, N + 1):
        # 构建更复杂的正则表达式
        # 开始标记: start_prefix-n-start_suffix
        # 捕获内容: (.*?)
        # 结束标记: end_prefix-n-end_suffix
        pattern = (
            f"{esc_start_prefix}-{n}-{esc_start_suffix}"
            r"(.*?)"  # 捕获组，非贪婪模式
            f"{esc_end_prefix}-{n}-{esc_end_suffix}"
        )
        
        # 使用 re.findall 进行查找
        # re.DOTALL (或 re.S) 是一个关键标志，它让 '.' 特殊字符可以匹配任何字符，包括换行符。
        matches = re.findall(pattern, input_str, re.DOTALL)
        
        if matches:
            # 对找到的每一个匹配项，使用 .strip() 去除其前后的空白字符（包括空格、制表符、换行符等）
            cleaned_matches = [match.strip() for match in matches]
            all_matches.extend(cleaned_matches)
            
    return all_matches