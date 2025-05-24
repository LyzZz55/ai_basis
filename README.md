# 第三部分输入输出

- User:来自用户输入：
- RAG:来自知识库：
- A{i}:来自以往 Agent

## 现有视觉资产评估与竞品分析

User(给 logo 图片，我来解析)

```json
brand_visual_assets_data = {
        "logo_description_str": "我们的Logo是一个复杂的盾牌和狮子图案，使用了三种深色调。",
        "vi_manual_summary_str": "VI手册规定了严格的线下物料配色和字体，线上应用提及较少。",
        "existing_colors_list_str": "['#1A2B3C', '#4D5E6F', '#7A8B9C']", # 品牌主色等
        "existing_fonts_list_str": "['宋体', '特定艺术字体']" # 现有字体
    }
```

A1:

```json
    brand_playbook_data = {
        "brand_persona_keywords_list_str": "['创新', '年轻', '活力', '科技感']",
        "brand_tone_descriptors_list_str": "['友好', '专业', '简洁']"
    }
```

**Out**

```json
    analysis_result = {
        "alignment_summary": "Logo图案与'科技感'人设部分匹配，但'复杂'特性与'简洁'语调存在冲突。VI手册对线上应用指导不足。",
        "digital_suitability_notes": "复杂Logo在小尺寸头像上可能难以识别。深色调配色需谨慎用于需要活力的社交平台。",
        "extensibility_issues": ["Logo横纵比不适合方形头像", "现有字体可能存在网页授权问题"],
        "adaptation_recommendations": ["建议简化Logo用于社交媒体", "考虑为线上补充更明亮的辅助色系"]
    }
```

## 建立 VI 系统

User(解析得到现有 VI、颜色、字体):

```json
brand_visual_assets_data
```

A1:

```json
    brand_playbook_data = {
        "brand_persona_keywords_list_str": "['创新', '年轻', '活力', '科技感']",
        "brand_tone_descriptors_list_str": "['友好', '专业', '简洁']"
    }
```

m2:

```json
"competitor_visual_strategies": [
   {"competitor_name": "竞品A","visual_summary": "明亮色彩、卡通形象、年轻化"},
   {"competitor_name": "竞品B", "visual_summary": "成熟稳重、实景摄影"},
   {"competitor_name": "竞品C", "visual_summary": "简约、科技感、深色背景、抽象线条"}
]

"identified_industry_trends": [
  {"name": "扁平化插画风", "description": "简洁、现代，常用于在线课程界面", "relevance_to_audience": "高 (符合'简约')"},
  {"name": "真实场景短视频", "description": "展现学习场景，提升代入感", "relevance_to_audience": "高 (符合'真实感'和'潮酷')"}
]

"social_media_specific_trends": { "trends_list": ["笔记式图文结合", "meme风格贴纸", "生活化场景短视频", "高饱和度配色"]  }
```

**Out**:

```json
 color_palette = {
        "primary_colors": [{"name": "BrandBlue", "hex": "#0A7AFF", "rgb": "10,122,255", "cmyk": "96,52,0,0", "use_case": "Logo主色, 核心按钮"}],
        "secondary_colors": [{"name": "SkyBlue", "hex": "#5AC8FA", "rgb": "90,200,250", "cmyk": "64,20,0,0", "use_case": "辅助图形, 背景点缀"}],
        "accent_colors": [{"name": "BrightYellow", "hex": "#FFD60A", "rgb": "255,214,10", "cmyk": "0,16,96,0", "use_case": "强调提示, CTA"}],
        "neutral_colors": [{"name": "LightGray", "hex": "#F2F2F7", "rgb": "242,242,247", "cmyk": "5,3,0,0", "use_case": "背景色"},
                           {"name": "DarkText", "hex": "#1C1C1E", "rgb": "28,28,30", "cmyk": "0,0,0,88", "use_case": "正文文本"}],
        "accessibility_notes": "主要文本与背景组合对比度已初步考虑，建议使用工具复核。"
    }

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
```

## 平台特化的视觉 prompt 设计

A2:

```json
Master_Editorial_Calendar_data: {
      "high_frequency_content_types": [ # Agent 2 可能提供这样的分析
        {"type_name": "产品上新公告", "platforms": ["微信公众号", "微博"], "frequency_score": 0.8},
        {"type_name": "用户故事分享", "platforms": ["小红书", "微信公众号"], "frequency_score": 0.7},
        {"type_name": "节日促销海报", "platforms": ["微博", "抖音"], "frequency_score": 0.9}
      ],
      "example_posts": [ # 或者提供具体帖子例子(但是容易出现幻觉，)
          {"id": "post001", "title": "春季新品上市！", "type": "产品上新公告", "platform": "微信公众号"},
          {"id": "post002", "title": "周末大促", "type": "节日促销海报", "platform": "微博"}
      ]
    }

```

m3:

```json
social_vi_system # m3输出的全部，能用就用
```

**Out**

```json
template_concepts_data: {
  content: str
  platform: str (平台)
  layout_description: str (布局描述)
  key_elements_description: str (关键元素描述)
  vi_application_notes: str (VI 应用说明)
}
```

## 生成图像

直接调用 gemini 的 API 生成即可

## 文案与图像协同

？？？

## 精细化发布策略

？？？？感觉没有必要，看 Agent2 给的内容日历精细程度了

## KPI 框架和报告结构

RAG:

```json


```

**Oout**

```
kpi_framework_and_reporting: dict 包含：
  detailed_kpis: list[dict] (KPI 名称, 类别, 定义, 计算公式构想, 平台相关性, 追踪工具建议)。
  reporting_template_outline: str (报告模板大纲)。


kpi_framework_output: {
      "detailed_kpi_library": [{"kpi_name": "曝光量...", "category": "认知层", ...}],
      "platform_specific_kpi_focus_map": {"Weibo": {"core_kpis_suggestion": [...], ...}},
      "reporting_template_structure_outline": {"suggested_reporting_frequency": "...", "core_sections": [...]},
      ...
    }
```

```json
flagship_content_creative_briefs_package: {
      "brief_001_summer_campaign": {
        "content_title": "夏日焕新活动",
        "goal": "提升夏季新品销量和品牌活力形象",
        "core_message": "清凉一夏，活力无限！发现你的夏日新装备。",
        "target_audience_segment": "年轻时尚人群",
        "desired_mood_and_tone": "活泼、明亮、充满动感、时尚",
        "key_visual_requirements_text": "需要一张主视觉海报，包含模特穿搭夏季新品在阳光沙滩的场景；系列产品展示图；短视频预告片概念。",
        "video_script_outline_text": "场景1: 阳光沙滩，模特奔跑。场景2: 产品特写，清凉感。场景3: Logo和活动日期。"
      },
      "brief_002_tech_explainer": {
          "content_title": "新品智能耳机深度解析",
          "goal": "展示产品技术亮点和创新功能",
          # ...更多字段...
      }
    }
```
