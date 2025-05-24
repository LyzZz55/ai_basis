# agent3/phase_2_vi_system_templates/module_3_social_vi_system.py
# from agent3.utils_knowledge_base_manager import load_knowledge_base_data

# --- Helper functions for sub-modules  ---
def _define_color_palette(
    existing_colors_str: str, # "['#000000', '#FFFFFF']"
    brand_tone_descriptors_str: str, # "['专业', '信赖']"
    audience_visual_preferences_str: str, # "['明亮', '现代']"
    industry_trends_data: list, # [{'trend_name': '莫兰迪色系', 'colors': ['#E0E0E0', '#BDBDBD']}]
    visual_design_principles_kb: dict
) -> dict:
    print("  模块3.1: 定义色彩体系...")
    # ... 详细逻辑参考阶段2大纲 ...
    # 示例简化输出:
    palette = {
        "primary_colors": [{"name": "BrandBlue", "hex": "#0A7AFF", "rgb": "10,122,255", "cmyk": "96,52,0,0", "use_case": "Logo主色, 核心按钮"}],
        "secondary_colors": [{"name": "SkyBlue", "hex": "#5AC8FA", "rgb": "90,200,250", "cmyk": "64,20,0,0", "use_case": "辅助图形, 背景点缀"}],
        "accent_colors": [{"name": "BrightYellow", "hex": "#FFD60A", "rgb": "255,214,10", "cmyk": "0,16,96,0", "use_case": "强调提示, CTA"}],
        "neutral_colors": [{"name": "LightGray", "hex": "#F2F2F7", "rgb": "242,242,247", "cmyk": "5,3,0,0", "use_case": "背景色"},
                           {"name": "DarkText", "hex": "#1C1C1E", "rgb": "28,28,30", "cmyk": "0,0,0,88", "use_case": "正文文本"}],
        "accessibility_notes": "主要文本与背景组合对比度已初步考虑，建议使用工具复核。"
    }
    # color_psychology = visual_design_principles_kb.get("color_psychology", {})
    # if "blue" in color_psychology and "BrandBlue" in str(palette):
    #     palette["psychology_notes"] = f"蓝色通常代表: {color_psychology['blue']}"
    return palette

def _define_typography_system(
    existing_fonts_str: str, # "['思源黑体 CN Regular', 'Arial']"
    brand_playbook_data: dict, # {'brand_persona_keywords_list_str': "['科技感', '现代']"}
    multi_language_needed: bool = False
) -> dict:
    print("  模块3.2: 定义字体系统...")
    # ... 详细逻辑参考阶段2大纲 ...
    # 示例简化输出:
    typography = {
        "primary_headline_font": {"family": "Montserrat", "weights_recommended": [700, 600], "style_description": "现代无衬线, 适用于数字标题"},
        "secondary_headline_font": {"family": "Roboto Slab", "weights_recommended": [700], "style_description": "可选衬线标题, 用于特定强调或复古感"},
        "body_text_font": {"family": "Open Sans", "weights_recommended": [400, 600], "style_description": "高易读性无衬线, 适用于正文和UI"},
        "typographic_scale_example": [
            {"element": "H1 (Page Title)", "font_family_ref": "primary_headline_font", "size_desktop": "32px", "size_mobile": "24px", "weight": 700, "line_height": 1.2},
            {"element": "Paragraph", "font_family_ref": "body_text_font", "size_desktop": "16px", "size_mobile": "14px", "weight": 400, "line_height": 1.6},
        ],
        "licensing_notes": "Montserrat, Roboto Slab, Open Sans 均为Google Fonts开源字体，可免费商用。"
    }
    if multi_language_needed:
        typography["language_support_notes"] = "所选字体对主流拉丁语系及部分CJK字符有良好支持，特殊语言需额外测试。"
    return typography

def _define_imagery_style_guide(
    brand_playbook_data: dict, # {'brand_tone_descriptors_list_str': "['真实', '亲切']"}
    audience_persona_data: dict, # {'visual_preferences_keywords_list_str': "['生活化场景', '明亮色调']"}
    trend_research_output: dict # from module 2
) -> dict:
    print("  模块3.3: 定义图像风格指南...")
    # ... 详细逻辑参考阶段2大纲 ...
    # 示例简化输出:
    imagery_guide = {
        "photography_style": {
            "overall_mood": "真实、亲切、积极向上，生活化场景为主。",
            "subject_matter": "优先展示真实用户在自然环境中使用产品的场景，或产品融入生活的美好瞬间。",
            "composition": "构图简洁、主体突出，鼓励使用自然光，营造明亮通透的视觉感受。",
            "color_palette_reference": "参考已定义的品牌色彩体系，整体色调和谐统一，可适当使用高光和暖调。",
            "dos_examples": ["捕捉自然的人物表情和互动", "图片清晰、焦点准确", "保持背景干净或有意义"],
            "donts_examples": ["使用过度修饰或虚假的摆拍图", "图片模糊或光线昏暗", "背景杂乱无章"]
        },
        "illustration_graphic_style": {
            "primary_style": "扁平化或轻拟物质感插画，线条流畅，色彩明快。",
            "iconography_style": "简约线性图标，与品牌字体风格协调，表意清晰。",
            "data_visualization_style": "图表设计简洁直观，色彩遵循品牌规范，避免过多装饰元素干扰信息传达。",
            "usage_notes": "插画可用于辅助解释复杂概念、增加趣味性或作为装饰元素。"
        }
    }
    return imagery_guide

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