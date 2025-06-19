########################################################
# 说明如何、何时、何地发布和推广内容。
########################################################

from dotenv import load_dotenv
import os
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")

def define_kpi_framework_and_reporting(
    initial_kpi_framework_data: dict,    # 来自Agent 1
    editorial_calendar_data: dict,       # 来自Agent 2
    brand_marketing_objectives_str: str, # 来自Agent 1 playbook (string representation of list)
    target_platforms: list
) -> dict:
    """
    定义详细的KPI框架、分析维度和报告模板建议。
    
    这里采取MCP，自己搜索相关的可行的API参数有哪些，根据平台关键词
    
    
    
    eg:
    initial_kpi_framework_data = {
        "primary_goals_list_str": "['提升品牌在线知名度', '增强用户社群活跃度']", # String representation of a list
        "secondary_goals_list_str": "['为官方网站引流', '收集潜在用户反馈']", # String representation of a list
        "suggested_key_metrics_awareness_list_str": "['总曝光量', '品牌提及增长率']",
        "suggested_key_metrics_engagement_list_str": "['平均互动率', 'UGC产出数量']",
        "measurement_period_suggestion_str": "月度追踪，季度复盘"
    }
    editorial_calendar_data = {
        "calendar_name_str": "Q3 2025 内容营销日历",
        "key_themes_list_str": "['夏日新品系列', '用户故事征集', '行业趋势解读']",
        "major_campaigns_list": [ # List of dictionaries
            {
                "campaign_name_str": "夏日焕新挑战赛",
                "duration_str": "2025-07-01 to 2025-07-31",
                "goal_str": "提升新品认知度与用户原创内容量",
                "target_platforms_list_str": "['小红书', '抖音']",
                "specific_kpi_focus_list_str": "['活动话题提及量', 'UGC作品提交数', '新品页面点击率']" # Agent 2 might suggest some focus KPIs
            },
            {
                "campaign_name_str": "科技前沿直播月",
                "duration_str": "2025-08-01 to 2025-08-31",
                "goal_str": "树立行业专家形象，收集销售线索",
                "target_platforms_list_str": "['B站', '微信视频号']",
                "specific_kpi_focus_list_str": "['直播观看人次', '平均观看时长', '互动评论数', '线索转化数']"
            }
        ],
        "common_content_formats_list_str": "['短视频', '图文笔记', '直播', '深度文章']",
        "notes_str": "内容日历侧重于提升品牌活力和用户参与感。"
    }
    brand_marketing_objectives_str = "['在未来6个月内将目标受众中的品牌认知度提升15%', '将社交媒体渠道的用户互动总数提升25% YoY', '通过社交媒体引流实现官网访问量月均增长10%', '将品牌在核心社交平台上的粉丝基数扩大20%']"
    
    target_platforms = ["Weibo", "Xiaohongshu", "Douyin", "Bilibili", "WeChat Official Account"]
    """
   
    print(f"模块8: 正在定义KPI框架与报告体系...")
    
    # 系统提示设计
    SystemPrompt = """
作为营销分析专家，你需要根据以下输入数据构建全面的KPI框架和报告体系：
1. 初始KPI框架数据 (initial_kpi_framework_data)
2. 内容日历数据 (editorial_calendar_data)
3. 品牌营销目标 (brand_marketing_objectives_str)
4. 目标平台列表 (target_platforms)

请严格按照以下JSON格式输出结果：
{
  "detailed_kpi_library": [
    {
      "kpi_name": "KPI名称",
      "category": "认知层/互动层/引导层/品牌健康度",
      "definition": "KPI定义",
      "formula_notes": "计算公式或说明",
      "platforms_applicable": ["适用平台1", "适用平台2"]
    }
  ],
  "platform_specific_kpi_focus_map": {
    "平台名称": {
      "core_kpis_suggestion": ["核心KPI1", "核心KPI2"],
      "secondary_kpis_suggestion": ["次要KPI1", "次要KPI2"],
      "diagnostic_kpis_notes": "诊断性KPI说明"
    }
  },
  "recommended_analysis_dimensions": ["分析维度1", "分析维度2"],
  "reporting_template_structure_outline": {
    "suggested_reporting_frequency": "报告频率",
    "core_sections": [
      {"section_name": "部分名称", "description": "部分描述"}
    ],
    "data_visualization_suggestions": ["可视化建议1", "可视化建议2"]
  },
  "data_tracking_tool_suggestions_notes": "数据追踪工具建议"
}

具体要求：
1. KPI库应覆盖认知层、互动层、引导层和品牌健康度四个类别
2. 平台KPI映射应基于平台特性（如微博重传播、小红书重互动、抖音重视频）
3. 分析维度应包含内容主题、平台对比、时间周期等
4. 报告结构应包含摘要、KPI达成、平台分析、内容分析等核心部分
5. 引用初始KPI框架中的指标建议和内容日历中的营销活动
6. 确保所有建议与品牌营销目标保持一致
"""


    # 创建模型实例
    model = ModelFactory.create(
        model_platform=ModelPlatformType.GEMINI,
        model_type=ModelType.GEMINI_2_0_FLASH,
        model_config_dict={"max_tokens": 4096, "temperature": 0.5},
        api_key=GEMINI_API_KEY,
    )
    
    # 创建Agent
    agent = ChatAgent(
        system_message=SystemPrompt,
        model=model,
        message_window_size=1000,
    )


    # 构建用户消息
    usr_msg = f"""
## 输入数据 ##

1. 初始KPI框架数据:
{json.dumps(initial_kpi_framework_data, indent=2, ensure_ascii=False)}

2. 内容日历数据:
{json.dumps(editorial_calendar_data, indent=2, ensure_ascii=False)}

3. 品牌营销目标:
{brand_marketing_objectives_str}

4. 目标平台列表:
{target_platforms}

## 特别说明 ##
- 请确保平台KPI映射考虑各平台特性：
  * 微博: 关注转发、评论、话题提及量
  * 小红书: 关注笔记互动（赞/藏/评）、收藏率
  * 抖音: 关注完播率、分享率、互动率
  * B站: 关注弹幕互动、平均观看时长
  * 微信公众号: 关注打开率、阅读完成率、转化CTR
- 对于内容日历中的营销活动，请创建相应的专项KPI
- 报告结构应包含季度复盘机制
"""
    
    try:
        # 获取Agent响应
        response = agent.step(usr_msg)
        raw_output = response.msgs[0].content
        
        # 清理响应内容
        if raw_output.startswith('```json'):
            clean_output = raw_output[7:-4].strip()
        elif raw_output.startswith('{'):
            clean_output = raw_output
        else:
            # 尝试提取JSON部分
            json_match = re.search(r'\{.*\}', raw_output, re.DOTALL)
            clean_output = json_match.group(0) if json_match else raw_output
        
        # 解析JSON
        kpi_framework = json.loads(clean_output)
        print(f"模块8: 成功生成KPI框架与报告体系")
        return kpi_framework
        
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}\n原始输出: {raw_output}")
        return {
            "detailed_kpi_library": [],
            "platform_specific_kpi_focus_map": {},
            "recommended_analysis_dimensions": [],
            "reporting_template_structure_outline": {},
            "data_tracking_tool_suggestions_notes": ""
        }
    except Exception as e:
        print(f"Agent执行错误: {e}")
        return {
            "detailed_kpi_library": [],
            "platform_specific_kpi_focus_map": {},
            "recommended_analysis_dimensions": [],
            "reporting_template_structure_outline": {},
            "data_tracking_tool_suggestions_notes": ""
        }
    

def test_define_kpi_framework_and_reporting():
    
    kpi_framework = define_kpi_framework_and_reporting(
        initial_kpi_framework_data={
            "primary_goals_list_str": "['提升品牌在线知名度', '增强用户社群活跃度']",
            "suggested_key_metrics_awareness_list_str": "['总曝光量', '品牌提及增长率']"
        },
        editorial_calendar_data={
            "major_campaigns_list": [
                {
                    "campaign_name_str": "夏日焕新挑战赛",
                    "target_platforms_list_str": "['小红书', '抖音']",
                    "specific_kpi_focus_list_str": "['活动话题提及量', 'UGC作品提交数']"
                }
            ]
        },
        brand_marketing_objectives_str="['在未来6个月内将品牌认知度提升15%']",
        target_platforms=["微博", "小红书", "抖音"]
    )
    # 输出结构示例
    print(kpi_framework["detailed_kpi_library"][0])


test_define_kpi_framework_and_reporting()
'''
{'kpi_name': '总曝光量', 'category': '认知层', 'definition': '所有平台品牌内容的总曝光次数，衡量品牌信息触达用户的广度。', 'formula_notes': '各平台曝光量加总。注意去重，避免重复计算。', 'platforms_applicable': ['微博', '小红书', '抖音']}
'''