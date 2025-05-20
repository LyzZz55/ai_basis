# 

## Nows
```json
{"competitor_visual_strategies": [{"competitor_name": "竞品 X", "visual_summary": "莫兰迪色系、流体质感插画、清新柔和"}, {"competitor_name": "竞品 Y", "visual_summary": "科技感、专业感、黑白色调、微距摄影展现护肤品质地"}], "identified_industry_trends": [{"name": "高级感莫兰迪配色", "description": "柔和低饱和度的色彩搭配，营造精致优雅的视觉氛围。", "relevance_to_audience": "高 (完全符合'高级感'和'柔和色调')"}, {"name": "产品特写与质感呈现", "description": "通过微距摄影或高清渲染，突出产品本身的质地和细节，强调品质感。", "relevance_to_audience": "高 (符合'质感肌理')"}, {"name": "极简主义排版设计", "description": "留白较多，信息层级清晰，强调视觉重点，营造干净利落的形象。", "relevance_to_audience": "高 (符合'极简线条')"}, {"name": "情绪化氛围营造", "description": "利用光影、色彩和构图，营造特定的情绪氛围，例如放松、治愈、自信等。", "relevance_to_audience": "中 (需要根据具体情绪与目标受众的需求匹配)"}], "social_media_specific_trends": {"微信公众号": ["简约排版", "高质量图片/视频", "产品使用前后对比", "用户真实测评分享"]}
```

 SystemAnalysePrompt = """
作为品牌策略分析专家，请根据以下提供的品牌视觉资产数据和品牌策略手册数据，评估当前品牌视觉资产与品牌战略（人设、语调）的匹配度，及其在数字媒体的适用性。

请严格按照以下JSON格式和内容要求输出您的分析结果, 不要出现多余的```json等包围, 输出为一行：

{"competitor_visual_strategies": [{"competitor_name": "从输入摘要中提取的竞品名称","visual_summary": "从输入摘要中总结该竞品的视觉特点"}],"identified_industry_trends": [{"name": "识别出的行业视觉趋势名称","description": "该趋势的简要描述","relevance_to_audience": "评估该趋势与目标受众视觉偏好的相关性（高/中/低），并可简要说明原因"}],"social_media_specific_trends": {"社交媒体平台名称1": ["该平台的主流视觉趋势1", "该平台的主流视觉趋势2"],"社交媒体平台名称2": ["该平台的主流视觉趋势1", "该平台的主流视觉趋势2"]}}


说明：
- `competitor_visual_strategies`: 需要从输入的 `agent1_competitor_analysis_summary_str` 中解析并分别列出主要竞品的视觉策略。
- `identified_industry_trends`: 结合 `brand_industry_str` 和 `target_audience_persona_data` 中的视觉偏好，列出当前行业内的主要视觉趋势及其与目标受众的匹配度。
- `social_media_specific_trends`: 针对 `social_media_platform_names_str` 中列出的社交媒体平台，分析其主流的视觉风格和趋势。

例如，如果输入是：
agent1_competitor_analysis_summary_str: "竞品A主要使用明亮色彩和卡通形象，风格年轻化。竞品B视觉风格偏向成熟稳重，使用大量实景摄影图片。竞品C则强调简约和科技感，采用深色背景和抽象线条。"
brand_industry_str: "在线教育"
target_audience_persona_data = {
  "audience_name": "Gen Z 学生",
  "visual_preferences_keywords_list_str": "['简约', '潮酷', '真实感', 'meme风格']"
}
social_media_platform_names_str: "微信公众号"

那么期望的输出可以为，但绝对不能出现别的```json ```等包围，只要JSON字符串：

{ "competitor_visual_strategies": [ {"competitor_name": "竞品A", "visual_summary": "明亮色彩、卡通形象、年轻化"}, {"competitor_name": "竞品B", "visual_summary": "成熟稳重、实景摄影"}, {"competitor_name": "竞品C", "visual_summary": "简约、科技感、深色背景、抽象线条"} ], "identified_industry_trends": [ {"name": "扁平化插画风", "description": "简洁、现代，常用于解释性内容和在线课程界面。", "relevance_to_audience": "中 (符合'简约')"}, {"name": "真实场景短视频", "description": "展现真实学习场景或用户故事，提升代入感。", "relevance_to_audience": "高 (符合'真实感'和'潮酷'，尤其在Gen Z中流行)"}, {"name": "动态数据可视化", "description": "用有趣动态图表展示学习成果或行业数据。", "relevance_to_audience": "中 (符合'简约'和'潮酷'，但需避免过于复杂)"}, {"name": "用户生成内容(UGC)风格", "description": "鼓励用户分享笔记、作品，视觉上强调真实和社区感。", "relevance_to_audience": "高 (符合'真实感'和'meme风格')"} ], "social_media_specific_trends": ["笔记式图文结合", "美观滤镜", "生活化学习场景分享"],  }

请确保输出是完整的 JSON 对象,没有别的包围
"""

##
不符合JSON语法规范mmd

## 
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
    
成了！

[{'competitor_name': '竞品 X', 'visual_summary': '莫兰迪色系、流体质感插画、清新柔和'}, {'competitor_name': '竞品 Y', 'visual_summary': '科技感、专业感、黑白色调、微距摄影展现护肤品质地'}]
[{'name': '高级感色彩搭配', 'description': '运用莫兰迪色、低饱和度色彩等，营造精致、优雅的视觉氛围', 'relevance_to_audience': "高 (符合'高级感'和'柔和色调')"}, {'name': '质感特写镜头', 'description': '通过微距摄影或高清渲染，突出产品质地和成分，增强视觉冲击力', 'relevance_to_audience': "高 (符合'质感肌理')"}, {'name': '极简主义排版', 'description': '采用简洁的字体和留白，突出产品和品牌信息，提升整体视觉舒适度', 'relevance_to_audience': "高 (符合'极简线条')"}]
{'trends_list': ['情绪化文案与场景化图片结合', '开箱测评类短视频', '真人试色/效果对比', '高颜值产品图', '干货知识分享']}


