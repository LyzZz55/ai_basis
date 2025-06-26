import os
from dotenv import load_dotenv
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
import json
from typing import Dict, Any, List

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")

def get_model(platform, model_type, api_key, max_tokens=4096, temperature=0.7):
    return ModelFactory.create(
        model_platform=platform,
        model_type=model_type,
        model_config_dict={
            "max_tokens": max_tokens,
            "temperature": temperature
        },
        api_key=api_key,
    )


dpsk_model = get_model(
    ModelPlatformType.SILICONFLOW,
    'Pro/deepseek-ai/DeepSeek-R1',
    SF_API_KEY,
    max_tokens=8192
)

import os
from dotenv import load_dotenv
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
import json
from typing import Dict, Any, List

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")

def get_model(platform, model_type, api_key, max_tokens=4096, temperature=0.7):
    return ModelFactory.create(
        model_platform=platform,
        model_type=model_type,
        model_config_dict={
            "max_tokens": max_tokens,
            "temperature": temperature
        },
        api_key=api_key,
    )

dpsk_model = get_model(
    ModelPlatformType.SILICONFLOW,
    'Pro/deepseek-ai/DeepSeek-R1',
    SF_API_KEY,
    max_tokens=8192
)

def refined_distribution_and_engagement_strategy(
    task: Dict[str, Any],
    trend_info: str = "",
    brand_story: str = "",
    audience_info: str = ""
) -> Dict[str, Any]:
    """
    针对单个内容任务，输出：
      - 精准发布时间窗口建议
      - 详细#标签矩阵策略（品牌/活动/内容/热门/长尾）
      - 具体互动引导和UGC激励细则
      - KOL/KOC初步合作方向和名单建议
      - 小额付费推广测试方案（平台、受众、形式、预算建议）
    """
    system_prompt = """
你是资深社交媒体内容分发与互动策略专家。请根据输入的内容任务、KPI目标、竞品趋势和受众信息，输出建议：
要求：
- 结合平台特性、内容主题、受众活跃时间、竞品做法和KPI目标，给出具体、可执行的建议。
- #标签矩阵要覆盖品牌、活动、内容、热门、长尾五类。
- 互动引导和UGC激励要有创意且易于执行。
- KOL/KOC名单可结合输入信息和行业常见类型。
- 预算建议要合理
"""
    user_input = f"""
内容任务:
{json.dumps(task, ensure_ascii=False)}

趋势:
{trend_info}

受众信息:
{audience_info}

品牌故事:
{brand_story}
"""
    
    try:
        response = dpsk_model.step(user_input)
        content = response.msgs[0].content
        # 清理可能的 markdown 代码块
        if content.strip().startswith("```json"):
            content = content.strip().split("```json")[-1].split("```")[0].strip()
        return json.loads(content)
    except Exception as e:
        return {"error": str(e)}
