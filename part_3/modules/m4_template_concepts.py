
from dotenv import load_dotenv
import os
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")


def design_visual_template_concepts(
    editorial_calendar_data: dict, # 来自Agent 2
    social_vi_system_output: dict, # 来自模块3
) -> list:
    """
    设计多平台视觉模板概念。
    """
    # editorial_calendar_data (输入示例): {
    #   "high_frequency_content_types": [ # Agent 2 可能提供这样的分析
    #     {"type_name": "产品上新公告", "platforms": ["微信公众号", "微博"], "frequency_score": 0.8},
    #     {"type_name": "用户故事分享", "platforms": ["小红书", "微信公众号"], "frequency_score": 0.7},
    #     {"type_name": "节日促销海报", "platforms": ["微博", "抖音"], "frequency_score": 0.9}
    #   ],
    #   "example_posts": [ # 或者提供具体帖子例子
    #       {"id": "post001", "title": "春季新品上市！", "type": "产品上新公告", "platform": "微信公众号"},
    #       {"id": "post002", "title": "周末大促", "type": "节日促销海报", "platform": "微博"}
    #   ]
    # }
    # social_vi_system_output (输入示例): output from module 3
    # target_platforms_str (输入示例): "['微信公众号', '微博', '小红书', '抖音']"

    print(f"模块4: 正在设计多平台视觉模板概念...")
    
    # 系统提示设计
    SystemPrompt = """
作为视觉设计系统架构师，你负责为品牌设计多平台视觉模板概念。请基于以下输入数据：
1. 内容日历数据（editorial_calendar_data）：包含高频内容类型和示例帖子
2. 品牌视觉系统（social_vi_system_output）：包含色彩、字体等规范
3. 目标平台列表（target_platforms）

请设计3-5个视觉模板概念，每个概念需包含以下字段：
- template_id: 模板唯一标识（如WCT_Product_V1）
- template_name: 模板名称
- target_platforms_formats: 适用的平台格式列表（如["微信公众号-头图(900x383px)"]）
- applicable_content_types: 适用的内容类型列表
- layout_description_textual: 布局文字描述
- key_visual_elements_placeholders: 关键视觉元素占位符列表
- color_application_notes: 色彩应用说明（需引用VI系统中的具体颜色名称）
- typography_application_notes: 字体应用说明（需引用VI系统中的具体字体）
- style_keywords: 风格关键词列表

输出要求：
1. 严格按JSON列表格式输出
2. 优先覆盖高频内容类型
3. 确保跨平台一致性
4. 引用VI系统中的具体元素
"""
    
    # 创建模型实例
    model = ModelFactory.create(
        model_platform=ModelPlatformType.GEMINI,
        model_type=ModelType.GEMINI_2_0_FLASH,
        model_config_dict={"max_tokens": 4096, "temperature": 0.7},
        api_key=GEMINI_API_KEY,
    )
    
    # 创建Agent
    agent = ChatAgent(
        system_message=SystemPrompt,
        model=model,
        message_window_size=1000,
    )

    # 1. 分析内容日历，选择3-5个重点模板进行概念设计 (简化逻辑)
    #    实际应用中会基于频率、重要性等进行筛选
    #    此处硬编码几个示例模板概念
    high_freq_content = editorial_calendar_data.get("high_frequency_content_types", [])
    if not high_freq_content and "example_posts" in editorial_calendar_data: # Fallback if no pre-analyzed types
        types_seen = {}
        for post in editorial_calendar_data["example_posts"]:
            key = (post["type"], post["platform"])
            types_seen[key] = types_seen.get(key, 0) + 1
        # Sort by frequency and pick top ones, simplified here
        if types_seen:
             high_freq_content.append({"type_name": list(types_seen.keys())[0][0], "platforms": [list(types_seen.keys())[0][1]], "frequency_score": 1})


    


    # visual_template_concepts_list (输出示例): [
    #   { "template_id": "WCT_Product_V1", "template_name": "微信图文-产品介绍模板系列", ... },
    #   { "template_id": "XHS_WB_Promo_V1", "template_name": "小红书/微博-促销活动模板", ... }
    # ]
    print(f"模块4: 多平台视觉模板概念设计完成，共计 {len(template_concepts_list)} 个模板概念。")
    return template_concepts_list