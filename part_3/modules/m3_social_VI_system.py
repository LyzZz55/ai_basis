# agent3/phase_2_vi_system_templates/module_3_social_vi_system.py
from dotenv import load_dotenv
import os
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
import json

# from agent3.utils_knowledge_base_manager import load_knowledge_base_data

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")


# --- Helper functions for sub-modules  ---
def _define_color_palette(
    existing_colors_str: str, # "['#000000', '#FFFFFF']"
    brand_tone_descriptors_str: str, # "['专业', '信赖']"
    audience_visual_preferences_str: str, # "['明亮', '现代']"
    industry_trends_data: list, # [{'trend_name': '莫兰迪色系', 'colors': ['#E0E0E0', '#BDBDBD']}]
    visual_design_principles_kb: dict
) -> dict:
    """
    基于品牌现有色彩、品牌语调、受众偏好、行业趋势和设计原则，智能生成品牌色彩体系建议。
    返回值: palette 字典，若AI返回异常则包含"error"字段。
    """
    print("  模块3.1: 定义色彩体系 (AI版)...")
    system_prompt = f"""
你是品牌视觉设计专家，请根据以下输入，智能生成适合社交媒体的品牌色彩体系建议，输出结构严格为JSON：
{{
  "primary_colors": [{{"name": "...", "hex": "...", "rgb": "...", "cmyk": "...", "use_case": "..."}}],
  "secondary_colors": [...],
  "accent_colors": [...],
  "neutral_colors": [...],
  "accessibility_notes": "...",
  "psychology_notes": "..."
}}
输入：
- 现有品牌主色: {existing_colors_str}
- 品牌语调描述: {brand_tone_descriptors_str}
- 受众视觉偏好: {audience_visual_preferences_str}
- 行业趋势色彩: {industry_trends_data}
- 设计原则知识: {visual_design_principles_kb.get('color_psychology', {})}
要求：
- 结合输入，推荐主色、辅助色、强调色、基础色，说明各自用途。
- 给出可访问性建议（如对比度、色盲友好等）。
- 给出色彩心理学简要说明。
- 输出必须是完整JSON对象，字段齐全。
"""
    model = ModelFactory.create(
        model_platform=ModelPlatformType.SILICONFLOW,
        model_type='Pro/deepseek-ai/DeepSeek-V3',
        model_config_dict={
            "max_tokens": 2048,
            "temperature": 0.7,
        },
        api_key=SF_API_KEY,
    )
    agent = ChatAgent(
        system_message=system_prompt,
        model=model,
        message_window_size=1000,
    )
    usr_msg = "请根据上述输入生成色彩体系建议。"
    try:
        response = agent.step(usr_msg)
        strRes = response.msgs[0].content
        try:
            return json.loads(strRes)
        except json.JSONDecodeError as e:
            return {"error": f"JSON解析错误: {e}", "raw": strRes}
    except Exception as e:
        return {"error": f"AI调用异常: {e}"}

def _define_typography_system(
    existing_fonts_str: str, # "['思源黑体 CN Regular', 'Arial']"
    brand_playbook_data: dict, # {'brand_persona_keywords_list_str': "['科技感', '现代']"}
    multi_language_needed: bool = False
) -> dict:
    """
    基于品牌现有字体、品牌人设、是否多语言需求，智能生成品牌字体体系建议。
    返回值: typography 字典，若AI返回异常则包含"error"字段。
    """
    print("  模块3.2: 定义字体系统 (AI版)...")
    persona_keywords = brand_playbook_data.get('brand_persona_keywords_list_str', '')
    tone_keywords = brand_playbook_data.get('brand_tone_descriptors_list_str', '')
    system_prompt = f"""
你是品牌视觉设计专家，请根据以下输入，智能生成适合社交媒体的品牌字体体系建议，输出结构严格为JSON：
{{
  "primary_headline_font": {{"family": "...", "weights_recommended": [...], "style_description": "..."}},
  "secondary_headline_font": {{"family": "...", "weights_recommended": [...], "style_description": "..."}},
  "body_text_font": {{"family": "...", "weights_recommended": [...], "style_description": "..."}},
  "typographic_scale_example": [{{"element": "...", "font_family_ref": "...", "size_desktop": "...", "size_mobile": "...", "weight": ..., "line_height": ...}}],
  "licensing_notes": "...",
  "language_support_notes": "..."
}}
输入：
- 现有品牌字体: {existing_fonts_str}
- 品牌人设关键词: {persona_keywords}
- 品牌语调关键词: {tone_keywords}
- 是否需要多语言支持: {multi_language_needed}
要求：
- 推荐主标题、次标题、正文字体，说明各自风格与用途。
- 给出字号、字重、行高等排版比例建议。
- 说明字体授权情况。
- 若multi_language_needed为True，需说明多语言支持情况。
- 输出必须是完整JSON对象，字段齐全。
"""
    model = ModelFactory.create(
        model_platform=ModelPlatformType.SILICONFLOW,
        model_type='Pro/deepseek-ai/DeepSeek-V3',
        model_config_dict={
            "max_tokens": 2048,
            "temperature": 0.7,
        },
        api_key=SF_API_KEY,
    )
    agent = ChatAgent(
        system_message=system_prompt,
        model=model,
        message_window_size=1000,
    )
    usr_msg = "请根据上述输入生成字体体系建议。"
    try:
        response = agent.step(usr_msg)
        strRes = response.msgs[0].content
        try:
            return json.loads(strRes)
        except json.JSONDecodeError as e:
            return {"error": f"JSON解析错误: {e}", "raw": strRes}
    except Exception as e:
        return {"error": f"AI调用异常: {e}"}

def _define_imagery_style_guide(
    brand_playbook_data: dict, # {'brand_tone_descriptors_list_str': "['真实', '亲切']"}
    audience_persona_data: dict, # {'visual_preferences_keywords_list_str': "['生活化场景', '明亮色调']"}
    trend_research_output: dict # from module 2
) -> dict:
    """
    基于品牌语调、受众偏好、行业趋势，智能生成品牌图像风格指南建议。
    返回值: imagery_guide 字典，若AI返回异常则包含"error"字段。
    """
    print("  模块3.3: 定义图像风格指南 (AI版)...")
    tone_keywords = brand_playbook_data.get('brand_tone_descriptors_list_str', '')
    audience_keywords = audience_persona_data.get('visual_preferences_keywords_list_str', '')
    industry_trends = trend_research_output.get('identified_industry_trends', [])
    system_prompt = f"""
你是品牌视觉设计专家，请根据以下输入，智能生成适合社交媒体的品牌图像风格指南建议，输出结构严格为JSON：
{{
  "photography_style": {{
    "overall_mood": "...",
    "subject_matter": "...",
    "composition": "...",
    "color_palette_reference": "...",
    "dos_examples": [...],
    "donts_examples": [...]
  }},
  "illustration_graphic_style": {{
    "primary_style": "...",
    "iconography_style": "...",
    "data_visualization_style": "...",
    "usage_notes": "..."
  }}
}}
输入：
- 品牌语调关键词: {tone_keywords}
- 受众视觉偏好: {audience_keywords}
- 行业趋势: {industry_trends}
要求：
- 明确摄影风格的整体氛围、主体、构图、色调、正反例。
- 明确插画/图标/数据可视化风格及用途。
- 输出必须是完整JSON对象，字段齐全。
"""
    model = ModelFactory.create(
        model_platform=ModelPlatformType.SILICONFLOW,
        model_type='Pro/deepseek-ai/DeepSeek-V3',
        model_config_dict={
            "max_tokens": 2048,
            "temperature": 0.7,
        },
        api_key=SF_API_KEY,
    )
    agent = ChatAgent(
        system_message=system_prompt,
        model=model,
        message_window_size=1000,
    )
    usr_msg = "请根据上述输入生成图像风格指南建议。"
    try:
        response = agent.step(usr_msg)
        strRes = response.msgs[0].content
        try:
            return json.loads(strRes)
        except json.JSONDecodeError as e:
            return {"error": f"JSON解析错误: {e}", "raw": strRes}
    except Exception as e:
        return {"error": f"AI调用异常: {e}"}

def _define_layout_principles(
    defined_color_system: dict,
    defined_typography_system: dict,
    visual_design_principles_kb: dict
) -> dict:
    print("  模块3.5: 定义版式与构图原则...")
    # ... 详细逻辑参考阶段2大纲 ...
    # layout_theory = visual_design_principles_kb.get("layout_theory", {})
    # 示例简化输出:
    layout_principles = {
        "grid_system_recommendation": "建议在设计中采用8点栅格系统，以保证元素对齐和间距的规范性。",
        "whitespace_utilization": "强调留白的价值，用于提升内容呼吸感、突出焦点、增强可读性。",
        "visual_hierarchy_guidelines": "通过字号、字重、色彩对比、空间关系等手段清晰区分信息层级。",
        "alignment_and_balance": "所有元素应有明确的对齐基准，追求视觉上的平衡感（对称或非对称）。",
        "logo_placement_rules_example": {
            "common_positions": ["左上角", "右上角", "底部居中 (特定场景)"],
            "minimum_clear_space": "Logo周围应保留至少相当于Logo高度50%的空白区域。",
            "minimum_size_on_social_post_image": "建议不小于整体图片宽度的10%或高度的5% (取较大者)"
        },
        "cross_platform_adaptability_notes": "设计时应考虑内容在不同屏幕尺寸和平台规范下的适应性，优先保证核心信息的可读性。"
    }
    return layout_principles

def build_social_vi_system(
    brand_visual_assets_data: dict,
    brand_playbook_data: dict,
    target_audience_persona_data: dict,
    module1_asset_analysis_output: dict, # 来自模块1
    module2_trend_research_output: dict, # 来自模块2
) -> dict:
    """
    构建完整的社交媒体视觉识别系统 (Social VI System)。
    """
    # brand_visual_assets_data (输入示例): from module 1
    # brand_playbook_data (输入示例): from module 1
    # target_audience_persona_data (输入示例): from module 2
    # module1_asset_analysis_output (输入示例): output of module 1
    # module2_trend_research_output (输入示例): output of module 2

    print(f"模块3: 正在构建社交媒体视觉识别系统 (Social VI System)...")
    visual_design_principles_kb = load_knowledge_base_data("visual_design_principles.json")

    # 调用内部辅助函数
    color_system = _define_color_palette(
        brand_visual_assets_data.get("existing_colors_list_str", "[]"),
        brand_playbook_data.get("brand_tone_descriptors_list_str", "[]"),
        target_audience_persona_data.get("visual_preferences_keywords_list_str", "[]"),
        module2_trend_research_output.get("identified_industry_trends", []),
        visual_design_principles_kb
    )
    typography_system = _define_typography_system(
        brand_visual_assets_data.get("existing_fonts_list_str", "[]"),
        brand_playbook_data,
        brand_playbook_data.get("multi_language_needed", False) # 假设从playbook获取
    )
    imagery_style_guide = _define_imagery_style_guide(
        brand_playbook_data,
        target_audience_persona_data,
        module2_trend_research_output
    )
    video_style_guide = _define_video_style_guide(
        brand_playbook_data,
        target_audience_persona_data,
        module2_trend_research_output
    )
    layout_principles = _define_layout_principles(
        color_system,
        typography_system,
        visual_design_principles_kb
    )

    social_vi_system_output = {
        "color_palette_system": color_system,
        "typography_system": typography_system,
        "imagery_style_guide": imagery_style_guide,
        "video_style_guide": video_style_guide,
        "layout_and_composition_principles": layout_principles,
        "version": "1.0",
        "creation_date": "2025-05-17" # Example date
    }
    # social_vi_system_output (输出示例): {
    #   "color_palette_system": {"primary_colors": [...], ...},
    #   "typography_system": {"primary_headline_font": {...}, ...},
    #   "imagery_style_guide": {"photography_style": {...}, ...},
    #   "video_style_guide": {"overall_pacing_and_mood": "...", ...},
    #   "layout_and_composition_principles": {"grid_system_recommendation": "...", ...},
    #   "version": "1.0", ...
    # }
    print(f"模块3: 社交媒体视觉识别系统构建完成。")
    return social_vi_system_output

def test_define_color_palette():
    # 测试样例
    existing_colors = "['#0A7AFF', '#FFD60A']"
    brand_tone = "['科技感', '信赖', '活力']"
    audience_pref = "['明亮', '现代', '高对比']"
    industry_trends = [
        {"trend_name": "莫兰迪色系", "colors": ['#E0E0E0', '#BDBDBD']},
        {"trend_name": "高饱和蓝", "colors": ['#0A7AFF']}
    ]
    visual_design_principles_kb = {"color_psychology": {"blue": "科技、信任、冷静", "yellow": "活力、乐观"}}
    res = _define_color_palette(existing_colors, brand_tone, audience_pref, industry_trends, visual_design_principles_kb)
    print(res)

def test_define_typography_system():
    # 测试样例
    existing_fonts = "['思源黑体 CN Regular', 'Arial']"
    brand_playbook = {
        'brand_persona_keywords_list_str': "['科技感', '现代', '国际化']",
        'brand_tone_descriptors_list_str': "['专业', '简洁']"
    }
    res = _define_typography_system(existing_fonts, brand_playbook, multi_language_needed=True)
    print(res)

def test_define_imagery_style_guide():
    # 测试样例
    brand_playbook = {
        'brand_tone_descriptors_list_str': "['真实', '亲切', '现代']"
    }
    audience_persona = {
        'visual_preferences_keywords_list_str': "['生活化场景', '明亮色调', '高质感']"
    }
    trend_research = {
        'identified_industry_trends': [
            {"name": "生活化摄影", "description": "真实场景、自然光"},
            {"name": "扁平插画", "description": "简洁明快"}
        ]
    }
    res = _define_imagery_style_guide(brand_playbook, audience_persona, trend_research)
    print(res)