# agent3/phase_4_distribution_performance/module_7_publishing_strategy.py

# --- Helper functions for sub-modules within Module 7 ---
def _suggest_publishing_times(audience_persona_data: dict, target_platforms: list, platform_characteristics_kb: dict) -> dict:
    print("  模块7.1: 建议最佳发布时间窗口...")
    recommendations = {}
    for platform in target_platforms:
        platform_general_peak = platform_characteristics_kb.get(platform, {}).get("peak_times_general", ["全天"])
        # audience_activity: "evenings during weekdays, afternoon on weekends"
        audience_activity_str = audience_persona_data.get("general_online_habits_summary_str", "")
        recommendations[platform] = {
            "based_on_persona_activity_str": audience_activity_str,
            "general_platform_peak_times": platform_general_peak,
            "combined_suggestion_notes": f"建议结合 '{audience_activity_str}' 和平台高峰 '{platform_general_peak}' 进行测试和选择。"
        }
    return {"publishing_time_recommendations": recommendations}

def _develop_advanced_hashtag_strategy(brand_playbook_data: dict, editorial_calendar_data: dict, industry_keywords_kb: dict) -> dict:
    print("  模块7.2: 制定高级#标签策略...")
    brand_name = brand_playbook_data.get("brand_name_str", "YourBrand")
    brand_primary_keywords = brand_playbook_data.get("brand_primary_keywords_list_str", "['核心价值1', '核心价值2']") # "['value1', 'value2']"
    try:
        brand_primary_keywords_list = eval(brand_primary_keywords)
    except:
        brand_primary_keywords_list = ["value1"]


    campaign_names = [c.get("name", f"Campaign{i+1}") for i, c in enumerate(editorial_calendar_data.get("campaigns", []))]
    content_pillars = brand_playbook_data.get("content_pillars_list_str", "['支柱1', '支柱2']") # "['pillar1', 'pillar2']"
    try:
        content_pillars_list = eval(content_pillars)
    except:
        content_pillars_list = ["pillar1"]


    strategy = {
        "brand_hashtags": [f"#{brand_name}"] + [f"#{brand_name}{kw}" for kw in brand_primary_keywords_list[:2]],
        "campaign_hashtags_examples": {name: [f"#{brand_name}{name}", f"#{name}活动"] for name in campaign_names},
        "content_pillar_hashtags_examples": {pillar: [f"#{brand_name}{pillar}", f"#{pillar}内容"] for pillar in content_pillars_list},
        "industry_specific_suggestions": industry_keywords_kb.get(brand_playbook_data.get("brand_industry_str", "DefaultIndustry"), ["#行业通用标签"]),
        "trending_hashtag_placeholder": "#[实时热门话题] (需人工或工具辅助查找)",
        "long_tail_hashtag_example": f"#{brand_name}用户真实体验",
        "usage_guidelines": "建议每条内容组合使用：1-2个品牌标签 + (若适用)1个活动标签 + 2-3个内容支柱/行业标签 + 1-2个热门/长尾标签。"
    }
    return {"hashtag_strategy_details": strategy}

def _design_interaction_ugc_incentives(editorial_calendar_data: dict, brand_playbook_data: dict, audience_persona_data: dict) -> dict:
    print("  模块7.3: 设计互动引导与UGC激励细则...")
    # Simplified: take one example content type or campaign
    example_content_type_for_ugc = editorial_calendar_data.get("example_content_for_ugc_str", "新品体验")
    brand_name = brand_playbook_data.get("brand_name_str", "YourBrand")
    audience_motivations_str = audience_persona_data.get("motivations_for_interaction_list_str", "['被认可', '获得奖励']") # "['recognition', 'rewards']"

    interaction_prompts = [
        f"你对我们的{example_content_type_for_ugc}有什么独到见解？在评论区告诉我们吧！",
        f"参与话题#{brand_name}创意互动#，赢取惊喜好礼！"
    ]
    ugc_campaign_example = {
        "campaign_name": f"{brand_name}创意{example_content_type_for_ugc}大赛",
        "theme": f"分享你与{brand_name}{example_content_type_for_ugc}的创意故事/用法",
        "participation_method_suggestion": f"发布图文/短视频并添加话题 #{brand_name}创意大赛# 和 @{brand_name}官方账号。",
        "judging_criteria_suggestion": ["创意性(40%)", "内容质量(30%)", "互动数据(30%)"],
        "reward_mechanism_suggestion": f"一等奖：最新款产品；二等奖：大额代金券；优秀参与奖：官方社媒平台展示机会。(基于受众动机 {audience_motivations_str})"
    }
    return {"interaction_prompts_examples": interaction_prompts, "ugc_campaign_example_details": ugc_campaign_example}

def _suggest_kol_koc_cooperation(kol_koc_list_data_str: str, flagship_content_briefs_package: dict, social_vi_system_output: dict) -> dict:
    print("  模块7.4: 初步KOL/KOC合作建议...")
    try:
        kol_koc_list = eval(kol_koc_list_data_str) # Example: "[{'name': 'KOL时尚小李', 'niche': '时尚穿搭', 'followers': '500k'}, {'name': 'KOC科技大王', 'niche': '数码评测', 'followers': '50k'}]"
    except:
        kol_koc_list = []

    suggestions = {}
    brand_visual_tone_summary = social_vi_system_output.get("imagery_style_guide", {}).get("photography_style", {}).get("overall_mood", "品牌调性")

    for brief_id, brief_data in flagship_content_briefs_package.items():
        brief_theme = brief_data.get("content_title", brief_id).lower() # Simplified theme
        matched_kols = []
        for kol in kol_koc_list:
            if kol.get("niche", "").lower() in brief_theme or brief_theme in kol.get("niche", "").lower(): # Simple match
                matched_kols.append({
                    "kol_name": kol.get("name"),
                    "kol_niche": kol.get("niche"),
                    "suggested_collaboration_type": "产品体验与评测帖/视频",
                    "cooperation_notes": f"合作内容需符合品牌视觉调性 ({brand_visual_tone_summary})，并突出'{brief_data.get('core_message', '产品核心卖点')}'。"
                })
        if matched_kols:
            suggestions[brief_id] = matched_kols
    
    if not suggestions and kol_koc_list: # Fallback if no specific match
        suggestions["general_kol_suggestion"] = [{
            "kol_name": kol_koc_list[0].get("name"), "kol_niche": kol_koc_list[0].get("niche"),
            "suggested_collaboration_type": "品牌联合活动",
            "cooperation_notes": f"可围绕近期主推内容或活动进行合作，保持{brand_visual_tone_summary}。"
        }]

    return {"kol_koc_preliminary_suggestions": suggestions}

def _suggest_paid_promotion_tests(flagship_content_briefs_package: dict, audience_persona_data: dict, budget_info_str: str, target_platforms: list, platform_characteristics_kb: dict) -> dict:
    print("  模块7.5: 初步付费推广建议...")
    # budget_info_str: "{'monthly_test_budget_range_usd': '500-1000', 'currency': 'USD'}"
    test_plans = {}
    default_budget_note = "建议进行小范围预算测试 (例如 $100-$300 per test) 来验证效果。"
    try:
        budget_details = eval(budget_info_str)
        budget_note = f"基于预算信息({budget_details.get('monthly_test_budget_range_usd', 'N/A')} {budget_details.get('currency', '')})，建议分配小部分进行A/B测试。"
    except:
        budget_note = default_budget_note


    for brief_id, brief_data in flagship_content_briefs_package.items():
        plan = {
            "content_brief_title_ref": brief_data.get("content_title", brief_id),
            "recommended_platforms_for_paid_test": [],
            "target_audience_segment_summary": brief_data.get("target_audience_segment", "基于核心用户画像"),
            "suggested_ad_formats": [],
            "key_message_for_ad_creative": brief_data.get("core_message", "突出核心价值"),
            "suggested_cta": "了解更多 /立即购买",
            "budget_and_testing_notes": budget_note
        }
        for platform in target_platforms:
            if platform in platform_characteristics_kb:
                plan["recommended_platforms_for_paid_test"].append(platform)
                plan["suggested_ad_formats"].extend(platform_characteristics_kb[platform].get("ad_formats", ["通用信息流广告"]))
        plan["suggested_ad_formats"] = list(set(plan["suggested_ad_formats"])) # Unique
        test_plans[brief_id] = plan
    
    if not test_plans and flagship_content_briefs_package: # Fallback
        first_brief_id = list(flagship_content_briefs_package.keys())[0]
        test_plans[first_brief_id] = {
            "content_brief_title_ref": flagship_content_briefs_package[first_brief_id].get("content_title", first_brief_id),
            "recommended_platforms_for_paid_test": target_platforms,
            "target_audience_segment_summary": "核心用户画像群体",
            "suggested_ad_formats": ["通用信息流广告"],
            "key_message_for_ad_creative": "突出核心价值",
            "suggested_cta": "了解详情",
            "budget_and_testing_notes": budget_note
        }


    return {"paid_promotion_preliminary_test_plans": test_plans}


def develop_refined_publishing_strategy(
    audience_persona_data: dict,        # From Agent 1
    brand_playbook_data: dict,          # From Agent 1
    editorial_calendar_data: dict,      # From Agent 2
    flagship_content_briefs_package: dict, # From Agent 2
    kol_koc_list_data_str: str,         # From Agent 1 (string representation of list)
    social_vi_system_output: dict,      # From Module 3
    budget_info_str: str,               # From Brand/User (string representation of dict)
    target_platforms: list              # e.g. ['Weibo', 'Xiaohongshu']
) -> dict:
    """
    整合精细化的发布策略与推广触点建议。
    """
    # audience_persona_data (输入示例): {'general_online_habits_summary_str': "工作日晚间及周末午后活跃", 'motivations_for_interaction_list_str': "['获取资讯', '优惠折扣']"}
    # brand_playbook_data (输入示例): {'brand_name_str': "示例品牌", 'brand_industry_str': "Tech", 'brand_primary_keywords_list_str': "['创新', '智能']", 'content_pillars_list_str': "['技术解读', '用户故事']"}
    # editorial_calendar_data (输入示例): {'campaigns': [{'name': '双十一大促', 'goal': '提升销量'}], 'example_content_for_ugc_str': "开箱视频"}
    # flagship_content_briefs_package (输入示例): from module 5
    # kol_koc_list_data_str (输入示例): "[{'name': '科技小明', 'niche': '数码评测', 'followers': '100k'}]"
    # social_vi_system_output (输入示例): from module 3
    # budget_info_str (输入示例): "{'monthly_test_budget_range_usd': '300-800', 'currency': 'USD'}"
    # target_platforms (输入示例): ['Weibo', 'Douyin', 'Bilibili']

    print(f"模块7: 正在制定精细化发布策略与推广建议...")
    platform_characteristics_kb = load_knowledge_base_data("platform_characteristics.json")
    industry_keywords_kb = load_knowledge_base_data("industry_keywords.json")

    publishing_times_output = _suggest_publishing_times(audience_persona_data, target_platforms, platform_characteristics_kb)
    hashtag_strategy_output = _develop_advanced_hashtag_strategy(brand_playbook_data, editorial_calendar_data, industry_keywords_kb)
    interaction_ugc_output = _design_interaction_ugc_incentives(editorial_calendar_data, brand_playbook_data, audience_persona_data)
    kol_koc_output = _suggest_kol_koc_cooperation(kol_koc_list_data_str, flagship_content_briefs_package, social_vi_system_output)
    paid_promo_output = _suggest_paid_promotion_tests(flagship_content_briefs_package, audience_persona_data, budget_info_str, target_platforms, platform_characteristics_kb)

    refined_strategy_output = {
        "best_publishing_time_windows": publishing_times_output,
        "advanced_hashtag_strategy": hashtag_strategy_output,
        "interaction_and_ugc_incentive_details": interaction_ugc_output,
        "kol_koc_cooperation_suggestions_preliminary": kol_koc_output,
        "paid_promotion_preliminary_suggestions": paid_promo_output,
        "strategy_summary_notes": "本策略整合了发布时间、标签、互动、KOL合作和付费推广的初步建议，需结合实际运营数据持续优化。"
    }
    # refined_strategy_output (输出示例): {
    #   "best_publishing_time_windows": {"publishing_time_recommendations": {"Weibo": {...}}},
    #   "advanced_hashtag_strategy": {"hashtag_strategy_details": {"brand_hashtags": [...]}},
    #   ...
    # }
    print(f"模块7: 精细化发布策略与推广建议制定完成。")
    return refined_strategy_output

