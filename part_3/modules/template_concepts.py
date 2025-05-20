
def design_visual_template_concepts(
    editorial_calendar_data: dict, # 来自Agent 2
    social_vi_system_output: dict, # 来自模块3
    target_platforms_str: str      # "['微信公众号', '微博', '小红书']"
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
    try:
        target_platforms_list = eval(target_platforms_str)
    except:
        target_platforms_list = ["微信公众号", "微博", "小红书"] # Default

    template_concepts_list = []

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


    # 示例模板1: 微信公众号文章头图/内页配图
    if "微信公众号" in target_platforms_list and ("产品上新公告" in str(high_freq_content) or not high_freq_content):
        template_concepts_list.append({
            "template_id": "WCT_Product_V1",
            "template_name": "微信图文-产品介绍模板系列",
            "target_platforms_formats": ["微信公众号-头图(900x383px)", "微信公众号-内文16:9配图", "微信公众号-正方形小图"],
            "applicable_content_types": ["新产品发布", "核心功能介绍", "品牌故事"],
            "layout_description_textual": "头图: 顶部品牌Logo(小号,参考VI布局原则), 中部产品主视觉(摄影风格参考VI), 底部Slogan/活动标题(字体参考VI H1/H2)。内文配图: 简洁明了, 图文结合紧密, 可采用左图右文或全宽图片。",
            "key_visual_elements_placeholders": ["产品高清图片", "生活方式场景图片", "核心卖点文字区", "CTA按钮样式占位"],
            "color_application_notes": f"主色调应用'{social_vi_system_output['color_palette_system']['primary_colors'][0]['name']}', 强调色用于CTA, 背景多用中性色。",
            "typography_application_notes": f"Slogan使用'{social_vi_system_output['typography_system']['primary_headline_font']['family']}' H1规范, 卖点文字使用H3规范。",
            "style_keywords": ["专业", "清晰", "品牌感强"]
        })

    # 示例模板2: 微博九宫格/小红书笔记封面+内页
    if ("微博" in target_platforms_list or "小红书" in target_platforms_list) and ("节日促销海报" in str(high_freq_content) or not high_freq_content):
        template_concepts_list.append({
            "template_id": "XHS_WB_Promo_V1",
            "template_name": "小红书/微博-促销活动模板",
            "target_platforms_formats": ["小红书-封面(3:4)", "小红书-内页方形图(1:1)", "微博-单图/九宫格(1:1)"],
            "applicable_content_types": ["节日促销", "限时优惠", "新品试用招募"],
            "layout_description_textual": "封面/主图: 强视觉冲击力, 产品或模特突出, 叠加醒目活动标题。内页/九宫格: 信息清晰, 价格、优惠方式、活动时间等元素规范排列。",
            "key_visual_elements_placeholders": ["吸引人的主视觉图片/短视频截图", "活动主标题", "副标题/活动详情", "价格标签样式", "二维码/参与方式占位"],
            "color_application_notes": f"多用'{social_vi_system_output['color_palette_system']['accent_colors'][0]['name']}'等强调色吸引眼球, 同时保持品牌色调的识别性。",
            "typography_application_notes": f"活动标题使用'{social_vi_system_output['typography_system']['primary_headline_font']['family']}' H1/H2规范, 促销信息文字层级分明。",
            "style_keywords": ["吸睛", "年轻化", "信息明确"]
        })
    # Add 1-3 more templates if needed, up to 3-5 total

    if not template_concepts_list: # Fallback if no specific matches
        template_concepts_list.append({
            "template_id": "GENERIC_SOCIAL_V1",
            "template_name": "通用社交媒体帖子模板",
            "target_platforms_formats": ["通用方形(1:1)", "通用横向(16:9)"],
            "applicable_content_types": ["日常问候", "快速资讯分享"],
            "layout_description_textual": "图片/视频区域 + 文字区域。Logo固定位置。",
            "key_visual_elements_placeholders": ["主视觉占位", "标题文字", "正文简述"],
            "color_application_notes": f"遵循'{social_vi_system_output['color_palette_system']['primary_colors'][0]['name']}'主色调。",
            "typography_application_notes": f"标题使用'{social_vi_system_output['typography_system']['primary_headline_font']['family']}'，正文使用'{social_vi_system_output['typography_system']['body_text_font']['family']}'。",
            "style_keywords": ["简洁", "通用"]
        })


    # visual_template_concepts_list (输出示例): [
    #   { "template_id": "WCT_Product_V1", "template_name": "微信图文-产品介绍模板系列", ... },
    #   { "template_id": "XHS_WB_Promo_V1", "template_name": "小红书/微博-促销活动模板", ... }
    # ]
    print(f"模块4: 多平台视觉模板概念设计完成，共计 {len(template_concepts_list)} 个模板概念。")
    return template_concepts_list