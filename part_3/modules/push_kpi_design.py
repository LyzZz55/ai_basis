########################################################
# 说明如何、何时、何地发布和推广内容。
########################################################

# from agent3.utils_knowledge_base_manager import load_knowledge_base_data

def define_kpi_framework_and_reporting(
    initial_kpi_framework_data: dict,    # 来自Agent 1
    editorial_calendar_data: dict,       # 来自Agent 2
    brand_marketing_objectives_str: str, # 来自Agent 1 playbook (string representation of list)
    target_platforms: list
) -> dict:
    """
    定义详细的KPI框架、分析维度和报告模板建议。
    """
    # initial_kpi_framework_data (输入示例): {'primary_goals_list_str': "['提升品牌知名度', '促进用户互动']", 'secondary_goals_list_str': "['引导官网流量']"}
    # editorial_calendar_data (输入示例): {'main_content_categories_list_str': "['产品介绍', '行业动态', '用户案例']", 'key_campaigns_for_tracking': [{'name': 'Q3新品推广', 'focus_kpis': ['新品提及量', '互动率']}]}
    # brand_marketing_objectives_str (输入示例): "['年度粉丝增长30%', '核心产品话题讨论度提升50%']"
    # target_platforms (输入示例): ['Weibo', 'Xiaohongshu', 'Douyin']

    print(f"模块8: 正在定义KPI框架与报告体系...")
    platform_analytics_kb = load_knowledge_base_data("platform_analytics_capabilities.json") # 假设包含各平台典型可追踪指标
    # platform_analytics_kb_example = {
    #    "Weibo": ["Impressions", "Engagement Rate", "Follower Growth", "CTR", "转发数", "评论数", "点赞数"],
    #    "Xiaohongshu": ["曝光量", "笔记互动（赞藏评）", "粉丝数", "主页访问量"],
    #    "Douyin": ["播放量", "完播率", "点赞", "评论", "分享", "主页访问"]
    # }


    kpi_definitions_list = [
        {"kpi_name": "曝光量/展示次数 (Impressions/Views)", "category": "认知层", "definition": "内容被展示的总次数。", "formula_notes": "平台直接提供", "platforms_applicable": target_platforms},
        {"kpi_name": "覆盖人数 (Reach)", "category": "认知层", "definition": "看到内容的独立用户总数。", "formula_notes": "平台直接提供", "platforms_applicable": target_platforms},
        {"kpi_name": "互动率 (Engagement Rate)", "category": "互动层", "definition": "（点赞+评论+分享+收藏等总互动数）/ 曝光量或覆盖人数。", "formula_notes": "需计算，确保分子分母一致性", "platforms_applicable": target_platforms},
        {"kpi_name": "点击率 (CTR - 若适用)", "category": "引导层", "definition": "点击链接的用户数 / 看到链接的用户数。", "formula_notes": "平台提供或通过短链追踪", "platforms_applicable": [p for p in target_platforms if p in ["Weibo", "微信公众号"]]}, # 示例
        {"kpi_name": "粉丝净增长数 (Net Follower Growth)", "category": "品牌健康度", "definition": "统计周期内新增粉丝数 - 流失粉丝数。", "formula_notes": "平台直接提供或计算", "platforms_applicable": target_platforms},
        {"kpi_name": "平均观看时长 (Avg. View Duration - 视频类)", "category": "互动层", "definition": "用户平均观看视频的时长。", "formula_notes": "平台直接提供", "platforms_applicable": [p for p in target_platforms if p in ["Douyin", "Bilibili", "快手"]]},
        # 可以根据 initial_kpi_framework_data 和 brand_marketing_objectives_str 动态添加更多KPI
    ]
    try:
        objectives = eval(brand_marketing_objectives_str)
        if any("知名度" in obj for obj in objectives):
            kpi_definitions_list.append({"kpi_name": "品牌搜索指数变化", "category": "认知层", "definition": "通过百度指数、微信指数等工具追踪品牌关键词搜索热度变化。", "formula_notes": "外部工具追踪", "platforms_applicable": ["Overall Brand"]})
    except:
        pass


    platform_kpi_mapping = {}
    for platform in target_platforms:
        core_kpis = []
        secondary_kpis = []
        platform_metrics = platform_analytics_kb.get(platform, []) # 从KB获取该平台典型指标
        if platform_metrics:
            core_kpis = platform_metrics[:len(platform_metrics)//2] # 简单取一半为核心
            secondary_kpis = platform_metrics[len(platform_metrics)//2:]
        else: # Fallback
            core_kpis = ["曝光量", "互动率"]
            secondary_kpis = ["粉丝净增长数"]
        platform_kpi_mapping[platform] = {
            "core_kpis_suggestion": core_kpis,
            "secondary_kpis_suggestion": secondary_kpis,
            "diagnostic_kpis_notes": "诊断性KPI需结合具体内容和目标，例如分析互动类型构成（评论vs点赞），或CTR的来源帖子。"
        }

    recommended_analysis_dimensions = [
        "按内容主题/系列", "按Persona画像 (若内容有明确区分)", "按发布时段/工作日vs周末",
        "按平台对比", "按内容格式 (图文vs短视频vs直播)", "按活动/营销节点", "付费推广vs自然流量"
    ]

    reporting_template_structure_outline = {
        "suggested_reporting_frequency": "周报（日常运营数据）、月报（趋势分析与策略调整）、季报（战略复盘）",
        "core_sections": [
            {"section_name": "1. 整体表现摘要 (Executive Summary)", "description": "关键指标概览、重要成果、主要问题与挑战。"},
            {"section_name": "2. 核心KPI达成情况 (Core KPI Performance)", "description": "对照目标（若有），展示核心KPI（认知、互动、引导、转化、品牌健康度）。"},
            {"section_name": "3. 各平台表现详析 (Platform Deep Dive)", "description": "分平台展示数据，对比各平台特性和用户行为差异。"},
            {"section_name": "4. 内容表现分析 (Content Performance Analysis)", "description": "按内容主题、格式等维度分析，找出优质内容和可优化方向。"},
            {"section_name": "5. 用户画像与互动分析 (Audience Insights)", "description": "粉丝增长趋势、用户画像变化、互动行为特点、UGC情况。"},
            {"section_name": "6. 营销活动效果评估 (Campaign Evaluation - 若有)", "description": "针对特定营销活动的目标达成情况进行专项评估。"},
            {"section_name": "7. 结论与行动建议 (Conclusion & Recommendations)", "description": "总结经验教训，提出下一阶段的优化策略和具体行动计划。"}
        ],
        "data_visualization_suggestions": ["趋势折线图 (如粉丝增长)", "对比柱状图 (如各平台互动率)", "构成饼图 (如互动类型占比)"]
    }

    kpi_framework_output = {
        "detailed_kpi_library": kpi_definitions_list,
        "platform_specific_kpi_focus_map": platform_kpi_mapping,
        "recommended_analysis_dimensions": recommended_analysis_dimensions,
        "reporting_template_structure_outline": reporting_template_structure_outline,
        "data_tracking_tool_suggestions_notes": "主要依赖各社交平台自带分析后台；可辅助使用第三方社交媒体管理工具、短链追踪、网站分析工具等。"
    }
    # kpi_framework_output (输出示例): {
    #   "detailed_kpi_library": [{"kpi_name": "曝光量...", "category": "认知层", ...}],
    #   "platform_specific_kpi_focus_map": {"Weibo": {"core_kpis_suggestion": [...], ...}},
    #   "recommended_analysis_dimensions": ["按内容主题...", ...],
    #   "reporting_template_structure_outline": {"suggested_reporting_frequency": "...", "core_sections": [...]},
    #   ...
    # }
    print(f"模块8: KPI框架与报告体系定义完成。")
    return kpi_framework_output
