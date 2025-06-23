
import sys
from pathlib import Path
# 获取项目根目录并添加到sys.path
project_root = str(Path(__file__).parent.parent.parent)  # 根据实际结构调整
sys.path.append(project_root)
# 使用绝对导入
from part_3.utils import load_file_config, load_files_from_config
from part_3.modules.m1_evaluate_existing_visual_assets import BrandVisualAnalyzer
from part_3.modules.m2_social_VI_system import VISystemDesignTeam, m2
from part_3.modules.m3_generate_image import generate_img, generate_main_visual_for_task_prompt
from part_3.modules.m4_kpi import kpi_working
from part_3.utils import setup_logger
from part_3.modules.Paser import contents_calendar_to_list

logger = setup_logger("GeneralControler", "tmp_log.log")




    








def perform_part_three():
    
    # 读取数据
    json_part_3_input = load_file_config("3_input_files/part_3_in.json") # TODO 不要写死
    logger.info(f"input config: {json_part_3_input}")
    needed_data_for_agent_three = load_files_from_config(json_part_3_input)
    logger.info(f"data for agent3 {needed_data_for_agent_three} ")
    
    # TODO 读取图片得到VI手册
    # img_style = 
    
    # M 1
    # m1 = BrandVisualAnalyzer()
    # # 评估现有 Logo、VI 手册等是否与 Agent 1 定义的品牌“人设”和“语调”匹配
    # visual_assets = m1.analyze_existing_visual_assets(
    #     needed_data_for_agent_three.get("3_input_files/1_brand_vi_manual.txt", ""),
    #     needed_data_for_agent_three.get("3_input_files/2_brand_story.txt", "Null"),
    # )
    # logger.info(visual_assets)
    # # {'alignment_summary': "Logo的复杂盾牌和狮子图案与品牌策略中强调的'技术可信度'和'环保承诺'部分匹配，但深色调与品牌策略中的'植物干细胞专利'和'纯素认证'所暗示的清新、自然感存在冲突。VI手册对线上应用的忽视与品牌在数字平台（如小红书、抖音）的高活跃度不匹配。", 'digital_suitability_notes': "复杂Logo在小尺寸头像上可能难以识别，尤其是在Instagram和小红书等平台上。深色调配色可能在需要展现活力和清新的社交平台上显得过于沉重。现有字体（如'特定艺术字体'）可能在数字媒体上的可读性和授权方面存在问题。", 'extensibility_issues': ['Logo横纵比不适合方形头像', '深色调配色在需要活力的平台上可能不吸引人', '现有字体可能存在网页授权问题', 'VI手册缺乏对线上应用的详细指导'], 'adaptation_recommendations': ['建议简化Logo用于社交媒体，保留核心元素以提高识别度', '考虑为线上补充更明亮、清新的辅助色系以增强活力感', '确保字体在数字媒体上的可读性和授权合规', '更新VI手册，增加对线上应用的详细规范和指导']}
    # # m1: 现有 Logo、VI 手册等是否适合在数字和社交媒体上传播
    # m1.research_visual_trends( needed_data_for_agent_three.get("./out/Comprehensive_Market_And_Competitor_Intelligence_Report.txt", "Null"))
    
    # m2
    m2_out = m2(
        needed_data_for_agent_three.get("3_input_files/2_brand_story.txt", "Null"),
        needed_data_for_agent_three.get("3_input_files/5_audience_personas.txt", "Null"),
    )
    logger.info("m2的输出： " + m2_out)
    
    
    # KPI生成
    kpi = kpi_working(
        needed_data_for_agent_three.get("3_input_files/7_kpi.txt", "Null"),
        needed_data_for_agent_three.get("3_input_files/2_brand_story.txt", "Null"),
        needed_data_for_agent_three.get("3_input_files/6_content_calendar.txt", "Null"),
    )
    logger.info("KPI的输出： " + m2_out)
    
    # 生成图片，根据内容日历
    
    contents_list = contents_calendar_to_list(
        needed_data_for_agent_three.get("3_input_files/6_content_calendar.txt", "Null"),
    )
    for single_task in contents_list.get('tasks', []):
        # 精细化发布策略
        # TODO
        
        # 主视觉生成
        img_prompt = generate_main_visual_for_task_prompt(single_task, vi_system=m2_out)
        generate_img(vi_system=m2_out, img_requirement=img_prompt, output_path=single_task.get('task_name', "tmp_res.png") )
    
    
#  **精细化发布策略与推广触点建议 (Refined Publishing Strategy & Promotion Touchpoint Suggestions):**
#       - **最佳发布时间窗口：** 结合 Agent 1 的受众分析和各平台特性，给出更精准的每日/每周最佳发布时间窗口建议（可细化到小时）。
#       - **高级#标签策略：** 除了通用和行业标签，建议品牌专属#标签，以及如何组合使用不同层级（热门、长尾、活动）的#标签矩阵以最大化曝光。
#       - **互动引导与 UGC 激励细化：** 针对不同内容类型，设计更具体的互动引导文案（如提问、投票、有奖评论）和 UGC 活动细则（如参与方式、评选标准、奖励机制）。
#       - **KOL/KOC 合作建议（初步）：** 基于 Agent 1 识别的 KOL/KOC 列表和 Agent 2 的内容规划，初步匹配合适的合作人选和合作内容方向（如产品测评、联合直播、内容共创）。
#       - **付费推广初步建议：** 针对旗舰内容或重点营销活动，建议在哪些平台、针对哪些受众画像、使用何种广告形式（如信息流广告、搜索广告、KOL 商单）进行小范围预算的付费推广测试。
    
    
perform_part_three()

