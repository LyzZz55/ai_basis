
def generate_ai_visual_prototyping_prompts(
    flagship_content_creative_briefs_package: dict, # 来自Agent 2
    social_vi_system_output: dict,                  # 来自模块3
    template_concepts_output: list,                 # 来自模块4
    # ai_tool_capabilities_kb: dict = None          # 可选
) -> dict:
    """
    为AI图像/视频工具生成文本提示 (Prompts)，用于视觉原型设计和风格探索。
    """
    # flagship_content_creative_briefs_package: {
    #   "brief_001_summer_campaign": {
    #     "content_title": "夏日焕新活动",
    #     "goal": "提升夏季新品销量和品牌活力形象",
    #     "core_message": "清凉一夏，活力无限！发现你的夏日新装备。",
    #     "target_audience_segment": "年轻时尚人群",
    #     "desired_mood_and_tone": "活泼、明亮、充满动感、时尚",
    #     "key_visual_requirements_text": "需要一张主视觉海报，包含模特穿搭夏季新品在阳光沙滩的场景；系列产品展示图；短视频预告片概念。",
    #     "video_script_outline_text": "场景1: 阳光沙滩，模特奔跑。场景2: 产品特写，清凉感。场景3: Logo和活动日期。"
    #   },
    #   "brief_002_tech_explainer": {
    #       "content_title": "新品智能耳机深度解析",
    #       "goal": "展示产品技术亮点和创新功能",
    #       # ...更多字段...
    #   }
    # }
    # social_vi_system_output (输入示例): output from module 3
    # template_concepts_output (输入示例): output from module 4

    print(f"模块5: 正在为AI视觉原型生成Prompts...")
    ai_prototyping_prompts_package = {"briefs": {}, "global_template_elements_prompts": {}}

    # 提取VI关键描述词
    primary_color_name = social_vi_system_output.get("color_palette_system", {}).get("primary_colors", [{}])[0].get("name", "brand_primary_color")
    accent_color_name = social_vi_system_output.get("color_palette_system", {}).get("accent_colors", [{}])[0].get("name", "brand_accent_color")
    photography_style_mood = social_vi_system_output.get("imagery_style_guide", {}).get("photography_style", {}).get("overall_mood", "professional")
    illustration_style_primary = social_vi_system_output.get("imagery_style_guide", {}).get("illustration_graphic_style", {}).get("primary_style", "modern flat")

    for brief_id, brief_data in flagship_content_creative_briefs_package.items():
        brief_prompts = {
            "content_title": brief_data.get("content_title", "N/A"),
            "mood_board_element_prompts": [],
            "key_visual_draft_prompts": [],
            "video_storyboard_prompts": []
        }

        desired_mood = brief_data.get("desired_mood_and_tone", photography_style_mood) # Fallback to VI

        # 1. Mood Board Element Prompts
        prompt_mood1 = f"Abstract mood board element representing '{desired_mood}', using colors {primary_color_name} and {accent_color_name}. Style: {photography_style_mood}, high detail, cinematic lighting."
        prompt_mood2 = f"Textured background in {primary_color_name} with {accent_color_name} accents, evoking a sense of '{brief_data.get('core_message', desired_mood)}'. Style: {illustration_style_primary}."
        brief_prompts["mood_board_element_prompts"].extend([prompt_mood1, prompt_mood2])

        # 2. Key Visual Draft Prompts
        key_visual_req = brief_data.get("key_visual_requirements_text", "")
        if "主视觉海报" in key_visual_req or "hero image" in key_visual_req:
            prompt_kv = f"Hero image for '{brief_data.get('content_title')}', theme: '{key_visual_req}'. Photography style: {photography_style_mood}, featuring {primary_color_name} and {accent_color_name}. Mood: {desired_mood}. Aspect ratio 16:9."
            brief_prompts["key_visual_draft_prompts"].append(prompt_kv)

        # 3. Video Storyboard Prompts
        video_script_outline = brief_data.get("video_script_outline_text", "")
        if video_script_outline:
            scenes = [s.strip() for s in video_script_outline.split("场景") if s.strip()] # 简易按场景分割
            for i, scene_desc_full in enumerate(scenes):
                try:
                    scene_num_desc, scene_action = scene_desc_full.split(":", 1)
                    scene_num = scene_num_desc.strip() # "1", "2" etc.
                except ValueError:
                    scene_num = str(i+1)
                    scene_action = scene_desc_full # Use full string if no colon

                prompt_video_scene = f"Video storyboard frame for '{brief_data.get('content_title')}', scene {scene_num}: {scene_action.strip()}. Visual style from VI: {social_vi_system_output.get('video_style_guide',{}).get('overall_pacing_and_mood','dynamic')}, key colors {primary_color_name}, {accent_color_name}."
                brief_prompts["video_storyboard_prompts"].append({
                    "scene_id": f"s{scene_num}",
                    "scene_description_from_brief": scene_action.strip(),
                    "generated_prompt": prompt_video_scene
                })
        ai_prototyping_prompts_package["briefs"][brief_id] = brief_prompts

    # 4. Template Element Prompts (Global or based on template_concepts_output)
    if template_concepts_output:
        first_template_id = template_concepts_output[0].get("template_id", "generic_template")
        ai_prototyping_prompts_package["global_template_elements_prompts"][f"icons_for_{first_template_id}"] = [
            f"Set of 5 minimalist line icons in {accent_color_name}, style: {social_vi_system_output.get('imagery_style_guide',{}).get('illustration_graphic_style',{}).get('iconography_style','simple line icon')}, representing themes: communication, innovation, community, quality, support."
        ]
        ai_prototyping_prompts_package["global_template_elements_prompts"][f"background_for_{first_template_id}"] = [
            f"Subtle geometric background texture using light {primary_color_name} and neutrals, style: {illustration_style_primary}, for social media posts."
        ]


    # ai_prototyping_prompts_package (输出示例): {
    #   "briefs": {
    #     "brief_001_summer_campaign": {
    #       "content_title": "夏日焕新活动",
    #       "mood_board_element_prompts": ["Abstract mood board element... ", "Textured background..."],
    #       "key_visual_draft_prompts": ["Hero image for '夏日焕新活动'..."],
    #       "video_storyboard_prompts": [
    #         {"scene_id": "s1", "scene_description_from_brief": "阳光沙滩，模特奔跑。", "generated_prompt": "Video storyboard frame for '夏日焕新活动', scene 1: ..."}
    #       ]
    #     }
    #   },
    #   "global_template_elements_prompts": {
    #       "icons_for_WCT_Product_V1": ["Set of 5 minimalist line icons..."]
    #    }
    # }
    print(f"模块5: AI视觉原型Prompts生成完成。")
    return ai_prototyping_prompts_package