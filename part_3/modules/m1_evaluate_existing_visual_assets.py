############################################
# 评估现有的视觉资产
# 与Agent 1定义的品牌“人设”和“语调”的匹配程度，分析其在数字和社交媒体上传播的潜力与局限性
############################################

from dotenv import load_dotenv
import os
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.configs import ChatGPTConfig, SiliconFlowConfig
from camel.types import ModelPlatformType, ModelType
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")



def analyze_existing_visual_assets(brand_visual_assets_data: dict, brand_playbook_data: dict) -> dict:
    '''
    评估当前品牌视觉资产与品牌战略（人设、语调）的匹配度，及其在数字媒体的适用性。

    输入eg:
    brand_visual_assets_data = {
        "logo_description_str": "我们的Logo是一个复杂的盾牌和狮子图案，使用了三种深色调。",
        "vi_manual_summary_str": "VI手册规定了严格的线下物料配色和字体，线上应用提及较少。",
        "existing_colors_list_str": "['#1A2B3C', '#4D5E6F', '#7A8B9C']", # 品牌主色等
        "existing_fonts_list_str": "['宋体', '特定艺术字体']" # 现有字体
    }

    brand_playbook_data = {
        "brand_persona_keywords_list_str": "['创新', '年轻', '活力', '科技感']",
        "brand_tone_descriptors_list_str": "['友好', '专业', '简洁']"
    }


    输出eg:
    analysis_result = {
        "alignment_summary": "Logo图案与'科技感'人设部分匹配，但'复杂'特性与'简洁'语调存在冲突。VI手册对线上应用指导不足。",
        "digital_suitability_notes": "复杂Logo在小尺寸头像上可能难以识别。深色调配色需谨慎用于需要活力的社交平台。",
        "extensibility_issues": ["Logo横纵比不适合方形头像", "现有字体可能存在网页授权问题"],
        "adaptation_recommendations": ["建议简化Logo用于社交媒体", "考虑为线上补充更明亮的辅助色系"]
    }
    '''
    # start of code analyze_existing_visual_assets
    
    SystemVisualImformationAnalysePrompt = """
作为品牌策略分析专家，请根据以下提供的品牌视觉资产数据和品牌策略手册数据，评估当前品牌视觉资产与品牌战略（人设、语调）的匹配度，及其在数字媒体的适用性。

请严格按照以下JSON格式和内容要求输出您的分析结果, 不要出现多余的```json等包围, 输出为一行：

{"alignment_summary": "总结品牌视觉资产（如Logo、VI手册）与品牌人设关键词和品牌语调描述词的整体匹配程度，指出一致和冲突之处。","digital_suitability_notes": "基于品牌视觉资产（如Logo复杂度、颜色）评估其在数字媒体（如小尺寸头像、社交平台）上的表现和潜在问题。","extensibility_issues": ["列出当前视觉资产在扩展应用到不同数字场景时可能遇到的具体问题，例如Logo的特定比例不适用于某种常见格式，或字体可能存在的授权问题等。"],"adaptation_recommendations": ["提出具体的优化建议，以增强品牌视觉资产在数字媒体的适用性和品牌战略的表达，例如建议简化某个元素，或补充新的视觉规范等。"]}


例如，如果输入是：

品牌视觉资产数据:
{
  "logo_description_str": "我们的Logo是一个复杂的盾牌和狮子图案，使用了三种深色调。",
  "vi_manual_summary_str": "VI手册规定了严格的线下物料配色和字体，线上应用提及较少。",
  "existing_colors_list_str": "['#1A2B3C', '#4D5E6F', '#7A8B9C']",
  "existing_fonts_list_str": "['宋体', '特定艺术字体']"
}
品牌策略手册数据:
{
  "brand_persona_keywords_list_str": "['创新', '年轻', '活力', '科技感']",
  "brand_tone_descriptors_list_str": "['友好', '专业', '简洁']"
}

那么期望的输出可以为：

{"alignment_summary": "Logo图案与'科技感'人设部分匹配，但'复杂'特性与'简洁'语调存在冲突。VI手册对线上应用指导不足。","digital_suitability_notes": "复杂Logo在小尺寸头像上可能难以识别。深色调配色需谨慎用于需要活力的社交平台。","extensibility_issues": ["Logo横纵比不适合方形头像", "现有字体可能存在网页授权问题"],"adaptation_recommendations": ["建议简化Logo用于社交媒体", "考虑为线上补充更明亮的辅助色系"]}

请确保输出是完整的 JSON 对象，并且每个字段的内容都经过深思熟虑，能够准确反映输入数据之间的关系和潜在的优化方向。
"""

    model = ModelFactory.create(
        model_platform=ModelPlatformType.SILICONFLOW,
        model_type='Pro/deepseek-ai/DeepSeek-V3',
        model_config_dict={
            "max_tokens": 4096,  # 设置合理的最大令牌数（根据模型支持调整）
            "temperature": 0.7,  # 可选：其他模型参数
        },
        api_key=SF_API_KEY,
    )
    
    agent = ChatAgent(
        system_message=SystemVisualImformationAnalysePrompt,
        model=model,
        message_window_size=1000,
    )
    usr_msg = f"""
品牌视觉资产数据:
{brand_visual_assets_data}
品牌策略手册数据:
{brand_playbook_data}
"""
    try:
        response = agent.step(usr_msg)
        strRes = response.msgs[0].content
        try:
            return json.loads(strRes)
        except json.JSONDecodeError as e:
            print(f"analyze_existing_visual_assets, JSON解析错误： {e}")
    except Exception as e:
        print(f"An error occured when ask for AI response: {e}")
    
    # end of code analyze_existing_visual_assets



def research_visual_trends(
    agent1_competitor_analysis_summary_str: str,
    brand_industry_str: str,
    target_audience_persona_data: dict,
    social_media_platform_names_str: str = "微信公众号"
) -> dict:
    '''
    研究竞品视觉策略及与品牌行业、目标受众相关的社交媒体视觉趋势。

    eg: 
    agent1_competitor_analysis_summary_str= "竞品A主要使用明亮色彩和卡通形象，风格年轻化。竞品B视觉风格偏向成熟稳重，使用大量实景摄影图片..."

    brand_industry_str= "在线教育" or "时尚快销"

    target_audience_persona_data = {
        "audience_name": "Gen Z 学生",
        "visual_preferences_keywords_list_str": "['简约', '潮酷', '真实感', 'meme风格']"
    }

    social_media_platform_names_list_str="['微信公众号', '微博', '小红书', '抖音']"

    输出：
    trend_report = {
        "competitor_visual_strategies": [
            {"competitor_name": "竞品A", "visual_summary": "明亮色彩、卡通形象、年轻化"},
            {"competitor_name": "竞品B", "visual_summary": "成熟稳重、实景摄影"}
        ],
        "identified_industry_trends": [
            {"name": "扁平化插画风", "description": "简洁、现代，常用于解释性内容", "relevance_to_audience": "中"},
            {"name": "明亮渐变色", "description": "营造积极、有活力的氛围", "relevance_to_audience": "高 (匹配'活力')"}
        ],
        "social_media_specific_trends":  ["生活化场景图", "精致排版"],
    }

    '''

    # begin of research_visual_trends
    SystemAnalysePrompt = """
作为品牌策略分析专家，请根据以下提供的品牌视觉资产数据和品牌策略手册数据，评估当前品牌视觉资产与品牌战略（人设、语调）的匹配度，及其在数字媒体的适用性。

请严格按照以下JSON格式和内容要求输出您的分析结果, 不要出现多余的```json等包围, 输出为一行：

{ "competitor_visual_strategies": [ {"competitor_name": "从输入摘要中提取的竞品名称","visual_summary": "从输入摘要中总结该竞品的视觉特点"} ], "identified_industry_trends": [ {"name": "识别出的行业视觉趋势名称","description": "该趋势的简要描述","relevance_to_audience": "评估该趋势与目标受众视觉偏好的相关性（高/中/低），并可简要说明原因"} ], "social_media_specific_trends": { "trends_list": [  // 统一键名，值为各平台主流视觉趋势的合并数组 "该平台的主流视觉趋势1", "该平台的主流视觉趋势2" ] } }


说明：
- `competitor_visual_strategies`: 需要从输入的 `agent1_competitor_analysis_summary_str` 中解析并分别列出主要竞品的视觉策略。
- `identified_industry_trends`: 结合 `brand_industry_str` 和 `target_audience_persona_data` 中的视觉偏好，列出当前行业内的主要视觉趋势及其与目标受众的匹配度。
- `social_media_specific_trends`: 针对 `social_media_platform_names_str` 中列出的社交媒体平台，**提取各平台共性视觉趋势**，合并到`trends_list`数组中（例如：微信公众号和抖音的共同趋势可统一列出）。

例如，如果输入是：
agent1_competitor_analysis_summary_str: "竞品A主要使用明亮色彩和卡通形象，风格年轻化。竞品B视觉风格偏向成熟稳重，使用大量实景摄影图片。竞品C则强调简约和科技感，采用深色背景和抽象线条。"
brand_industry_str: "在线教育"
target_audience_persona_data = {
  "audience_name": "Gen Z 学生",
  "visual_preferences_keywords_list_str": "['简约', '潮酷', '真实感', 'meme风格']"
}
social_media_platform_names_str: "微信公众号,抖音"

那么期望的输出为：

{ "competitor_visual_strategies": [ {"competitor_name": "竞品A", "visual_summary": "明亮色彩、卡通形象、年轻化"}, {"competitor_name": "竞品B", "visual_summary": "成熟稳重、实景摄影"}, {"competitor_name": "竞品C", "visual_summary": "简约、科技感、深色背景、抽象线条"} ], "identified_industry_trends": [ {"name": "扁平化插画风", "description": "简洁、现代，常用于在线课程界面", "relevance_to_audience": "高 (符合'简约')"}, {"name": "真实场景短视频", "description": "展现学习场景，提升代入感", "relevance_to_audience": "高 (符合'真实感'和'潮酷')"} ], "social_media_specific_trends": { "trends_list": ["笔记式图文结合", "meme风格贴纸", "生活化场景短视频", "高饱和度配色"]  // 合并多平台趋势 } }

请确保输出是完整的 JSON 对象，并且每个字段的内容都经过深入研究和分析，能够准确反映当前视觉趋势。
"""
    
    model = ModelFactory.create(
        model_platform=ModelPlatformType.GEMINI,
        model_type=ModelType.GEMINI_2_0_FLASH,
        model_config_dict={
            "max_tokens": 4096,  # 设置合理的最大令牌数（根据模型支持调整）
            "temperature": 0.7,  # 可选：其他模型参数
        },
        api_key=GEMINI_API_KEY,
    )
    
    agent = ChatAgent(
        system_message=SystemAnalysePrompt,
        model=model,
        message_window_size=1000,
    )
    usr_msg = f"""
agent1_competitor_analysis_summary_str: {agent1_competitor_analysis_summary_str}
brand_industry_str: {brand_industry_str}
target_audience_persona_data = {target_audience_persona_data}
social_media_platform_names_str: {social_media_platform_names_str}
        """
    try:
        response = agent.step(usr_msg)
        strRes = response.msgs[0].content
        if (strRes[0] == '`'):
            strRes = strRes[7: -4]
        try:
            return json.loads(strRes)
        except json.JSONDecodeError as e:
            print(f"analyze_existing_visual_assets, JSON解析错误： {e}")
    except Exception as e:
            print(f"An error occured when ask for AI response: {e}")
    
    

    
    # end of research_visual_trends


##################################################################################################################################
##################################################################################################################################
########################                          TESTS                   ########################################################
##################################################################################################################################
##################################################################################################################################



def test_analyze_existing_visual_assets():
    a = {
        "logo_description_str": "我们的 Logo 是一个复古的面包篮和麦穗图案，使用了三种暖色调。",
        "vi_manual_summary_str": "VI 手册规定了严格的包装配色和手写字体，线上店铺视觉提及较少。",
        "existing_colors_list_str": "['#F2D1A5', '#E6B37B', '#D9954F']", 
        "existing_fonts_list_str": "[' 汉仪粗圆体 ', ' 定制手写字体 ']"
    }
    
    b = {
        "brand_persona_keywords_list_str": "[' 传统 ', ' 温馨 ', ' 自然 ', ' 手工感 ']", 
        "brand_tone_descriptors_list_str": "[' 亲切 ', ' 治愈 ', ' 质朴 ']" 
    }
    
    res = analyze_existing_visual_assets(a, b)
    print(res["alignment_summary"])
    print(res["digital_suitability_notes"])
    print(res["extensibility_issues"])

    



def test_research_visual_trends():
    
    a = "竞品 X 主要使用莫兰迪色系与流体质感插画，风格清新柔和。竞品 Y 视觉风格偏向科技感与专业感，以黑白色调为主，结合微距摄影展现护肤品质地"
    b = "美妆护肤"
    t = {
        "audience_name": "千禧代职场女性",
        "visual_preferences_keywords_list_str": "[' 高级感 ', ' 柔和色调 ', ' 质感肌理 ', ' 极简线条 ']"
    }
    s = [
        "微信公众号", "小红书"
    ]
    
    res = research_visual_trends(a, b, t, s[0])
    print(res['competitor_visual_strategies'])
    print(res['identified_industry_trends'])
    print(res['social_media_specific_trends'])
    
# test_analyze_existing_visual_assets()
# print('\n')
# test_research_visual_trends()
'''
>>> test_analyze_existing_visual_assets()
>>> print('\n')
>>> test_research_visual_trends()

Logo的面包篮和麦穗图案与'传统'、'自然'、'手工感'人设高度匹配，暖色调与'温馨'、'治愈'语调完美契合。VI手册对线上店铺视觉指导不足，可能影响数字媒体的一致性。
复古Logo在小尺寸头像上可能细节丢失，暖色调在数字媒体上表现良好但需注意对比度。手写字体在移动端可能不易阅读。
['Logo细节可能在小尺寸下难以辨认', '定制手写字体可能不适合所有数字平台', '暖色调在部分屏幕显示可能偏色']

[{'competitor_name': '竞品 X', 'visual_summary': '莫兰迪色系、流体质感插画、清新柔和'}, {'competitor_name': '竞品 Y', 'visual_summary': '科技感、专业感、黑白色调、微距摄影展现护肤品质地'}]
[{'name': '高级感色彩搭配', 'description': '运用莫兰迪色、低饱和度色彩等，营造精致、优雅的视觉氛围', 'relevance_to_audience': "高 (符合'高级感'和'柔和色调')"}, {'name': '质感特写镜头', 'description': '通过微距摄影或高清渲染，突出产品质地和成分，增强视觉冲击力', 'relevance_to_audience': "高 (符合'质感肌理')"}, {'name': '极简主义排版', 'description': '采用简洁的字体和留白，突出产品和品牌信息，提升整体视觉舒适度', 'relevance_to_audience': "高 (符合'极简线条')"}]
{'trends_list': ['情绪化文案与场景化图片结合', '开箱测评类短视频', '真人试色/效果对比', '高颜值产品图', '干货知识分享']}

'''
