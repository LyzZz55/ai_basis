########################################################################################
# 评估现有的视觉资产
# 与Agent 1定义的品牌“人设”和“语调”的匹配程度，分析其在数字和社交媒体上传播的潜力与局限性
# 分析竞品视觉策略，研究与品牌行业和目标受众相关的社交媒体视觉设计趋势
########################################################################################

from colorama import Fore

from camel.societies import RolePlaying
from camel.utils import print_text_animated
from camel.models import ModelFactory
from camel.toolkits import FunctionTool 
from camel.toolkits import SearchToolkit  
from camel.types import ModelPlatformType, ModelType

from camel.agents import ChatAgent
import json

from utils import clean_json_string

import os
from dotenv import load_dotenv
load_dotenv()
SF_API_KEY = os.getenv("FLOW_API")

visual_analysis_model = ModelFactory.create(
    model_platform=ModelPlatformType.SILICONFLOW,
    model_type='Pro/deepseek-ai/DeepSeek-V3',
    model_config_dict={
        "max_tokens": 8192,
        "temperature": 0.7
    },
    api_key=SF_API_KEY,
)

search_toolkit = SearchToolkit()  
search_tools = [  
    FunctionTool(search_toolkit.search_duckduckgo),  
    FunctionTool(search_toolkit.search_google),  
]

visual_trends_agent = ChatAgent(  
    model=visual_analysis_model,   
    tools=search_tools,  
    system_message="你是一个专业的社交媒体视觉趋势研究专家，擅长分析品牌行业和目标受众的视觉设计趋势。"  
)  

def research_visual_trends(
    cur_brand_story_industry_analysis: str,
) -> dict:
  
    query = f"""  
    请研究行业的社交媒体视觉设计趋势。根据下面信息：
    {cur_brand_story_industry_analysis}
    重点关注：  
    1. 当前流行的视觉设计元素  
    2. 色彩搭配趋势  
    3. 排版和布局风格  
      
    """  
    response = visual_trends_agent.step(query)  
    return response.msgs[0].content  
