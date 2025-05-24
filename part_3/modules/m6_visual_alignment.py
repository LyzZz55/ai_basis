
def review_copy_visual_alignment(
    draft_copy_package_data: dict,        # 来自Agent 2
    master_editorial_calendar_data: dict, # 来自Agent 2 (用于上下文关联)
    social_vi_system_output: dict,        # 来自模块3
    ai_prototyping_prompts_package: dict  # 来自模块5
) -> dict:
    """
    审核文案与规划的视觉方向是否匹配，并提出优化建议。
    """
    # draft_copy_package_data (输入示例): {
    #   "content_item_XYZ001": { # ID 通常来自内容日历或brief
    #     "brief_id_ref": "brief_001_summer_campaign", # 关联到模块5的brief
    #     "draft_copy_A_text": "夏日炎炎，激情不减！快来参加我们的'夏日焕新'活动，全场新品限时8折...",
    #     "draft_copy_B_text": "清凉一夏，从新开始。我们的夏季系列为你带来无与伦比的舒适与时尚..."
    #   },
    #   "content_item_ABC002": {
    #     "brief_id_ref": "brief_002_tech_explainer",
    #     "draft_copy_A_text": "本文将深入剖析我们最新智能耳机的声学架构、降噪技术以及创新的手势交互...",
    #   }
    # }
    # master_editorial_calendar_data (输入示例): { "posts": [{"id": "content_item_XYZ001", "title": "夏日焕新", "brief_id": "brief_001_summer_campaign"}] }
    # social_vi_system_output (输入示例): output from module 3
    # ai_prototyping_prompts_package (输入示例): output from module 5

    print(f"模块6: 正在审核文案与视觉匹配度...")
    copy_visual_alignment_report = {}

    for item_id, copy_data in draft_copy_package_data.items():
        brief_id_ref = copy_data.get("brief_id_ref")
        current_copy_text = copy_data.get("draft_copy_A_text", "") # 以A稿为例

        visual_mood_from_vi = social_vi_system_output.get("imagery_style_guide", {}).get("photography_style", {}).get("overall_mood", "professional")
        planned_visual_prompts_for_item = ai_prototyping_prompts_package.get("briefs", {}).get(brief_id_ref, {})
        
        # 提取brief中期望的情绪，如果AI prompts里有更具体的，也可以参考
        brief_desired_mood = ""
        if brief_id_ref and brief_id_ref in ai_prototyping_prompts_package.get("briefs", {}):
             # This assumes flagship_content_creative_briefs_package was an input to module 5 and its structure is known
             # or that mood is somehow embedded in the prompts package structure.
             # For simplicity, let's assume mood is part of the VI or can be inferred.
             pass


        analysis_notes = []
        optimization_suggestions = []
        alignment_status = "待评估"

        # 1. 基调与情绪匹配 (简化逻辑)
        copy_tone_is_playful = any(word in current_copy_text for word in ["激情", "活力", "快来"])
        visual_tone_is_playful = "活泼" in visual_mood_from_vi or "动感" in visual_mood_from_vi or (brief_desired_mood and "活泼" in brief_desired_mood)

        if copy_tone_is_playful and not visual_tone_is_playful:
            analysis_notes.append("文案语调活泼，但当前整体视觉风格定义偏专业，可能存在不协调。")
            optimization_suggestions.append({"type": "visual_or_copy", "suggestion": "考虑调整视觉风格使其更活泼，或调整文案语调以匹配专业视觉。"})
            alignment_status = "需要改进"
        elif not copy_tone_is_playful and visual_tone_is_playful:
            analysis_notes.append("视觉风格规划偏活泼，但文案语调较为平实。")
            optimization_suggestions.append({"type": "copy", "suggestion": "建议文案增加一些活力元素。"})
            alignment_status = "需要改进"
        else:
            analysis_notes.append("文案与视觉基调初步匹配。")
            alignment_status = "良好"

        # 2. 信息支撑与一致性
        if "沙滩" in current_copy_text.lower() and planned_visual_prompts_for_item: # 假设文案提到沙滩
            # 检查key visual prompts是否包含沙滩
            has_beach_visual = False
            for prompt in planned_visual_prompts_for_item.get("key_visual_draft_prompts", []):
                if "沙滩" in prompt.lower() or "beach" in prompt.lower():
                    has_beach_visual = True
                    break
            if not has_beach_visual:
                analysis_notes.append("文案提及'沙滩'，但关键视觉的AI Prompts中未明确体现此场景。")
                optimization_suggestions.append({"type": "visual_prompt", "suggestion": "建议在关键视觉的AI Prompt中加入'沙滩'元素，或确认是否有其他视觉素材支持此描述。"})
                if alignment_status == "良好": alignment_status = "良好，有微调建议"


        if not analysis_notes:
            analysis_notes.append("文案与视觉规划在关键信息点上基本一致。")

        copy_visual_alignment_report[item_id] = {
            "copy_reference_text_snippet": current_copy_text[:100] + "...",
            "visual_plan_summary_ref": f"Refers to VI mood '{visual_mood_from_vi}' and prompts for brief '{brief_id_ref}' in AI prompts package.",
            "alignment_status": alignment_status,
            "analysis_notes": analysis_notes,
            "optimization_suggestions": optimization_suggestions if optimization_suggestions else ["暂无具体优化建议，整体匹配度较好。"]
        }

    # copy_visual_alignment_report (输出示例): {
    #   "content_item_XYZ001": {
    #     "copy_reference_text_snippet": "夏日炎炎，激情不减...",
    #     "visual_plan_summary_ref": "Refers to VI mood '活泼、明亮' and prompts for brief 'brief_001_summer_campaign'...",
    #     "alignment_status": "良好，有微调建议",
    #     "analysis_notes": ["文案与视觉基调初步匹配。", "文案提及'沙滩'，但关键视觉的AI Prompts中未明确体现此场景。"],
    #     "optimization_suggestions": [{"type": "visual_prompt", "suggestion": "建议在关键视觉的AI Prompt中加入'沙滩'元素..."}]
    #   }
    # }
    print(f"模块6: 文案与视觉匹配度审核完成。")
    return copy_visual_alignment_report
