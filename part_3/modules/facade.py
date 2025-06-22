
import sys
from pathlib import Path
# 获取项目根目录并添加到sys.path
project_root = str(Path(__file__).parent.parent.parent)  # 根据实际结构调整
sys.path.append(project_root)
# 使用绝对导入
from part_3.utils import load_file_config, load_files_from_config
from part_3.modules.m1_evaluate_existing_visual_assets import BrandVisualAnalyzer
from part_3.modules.m2_social_VI_system import VISystemDesignTeam, m2

def perform_part_three():
    
    # 读取数据
    json_part_3_input = load_file_config("./out/part_3_in.json")
    # print(json_part_3_input)
    needed_data_for_agent_three = load_files_from_config(json_part_3_input)
    # print(needed_data_for_agent_three)
    
   # M 1
    # m1 = BrandVisualAnalyzer()
    # 评估现有 Logo、VI 手册等是否与 Agent 1 定义的品牌“人设”和“语调”匹配
    brand_visual_assets_data = {
            "logo_description_str": "我们的Logo是一个复杂的盾牌和狮子图案，使用了三种深色调。",
            "vi_manual_summary_str": "VI手册规定了严格的线下物料配色和字体，线上应用提及较少。",
            "existing_colors_list_str": "['#1A2B3C', '#4D5E6F', '#7A8B9C']", # 品牌主色等
            "existing_fonts_list_str": "['宋体', '特定艺术字体']" # 现有字体
    }
    # visual_assets = m1.analyze_existing_visual_assets(brand_visual_assets_data, needed_data_for_agent_three.get("./out/Comprehensive_Market_And_Competitor_Intelligence_Report.txt", "Null"))
    # print(visual_assets)
    # {'alignment_summary': "Logo的复杂盾牌和狮子图案与品牌策略中强调的'技术可信度'和'环保承诺'部分匹配，但深色调与品牌策略中的'植物干细胞专利'和'纯素认证'所暗示的清新、自然感存在冲突。VI手册对线上应用的忽视与品牌在数字平台（如小红书、抖音）的高活跃度不匹配。", 'digital_suitability_notes': "复杂Logo在小尺寸头像上可能难以识别，尤其是在Instagram和小红书等平台上。深色调配色可能在需要展现活力和清新的社交平台上显得过于沉重。现有字体（如'特定艺术字体'）可能在数字媒体上的可读性和授权方面存在问题。", 'extensibility_issues': ['Logo横纵比不适合方形头像', '深色调配色在需要活力的平台上可能不吸引人', '现有字体可能存在网页授权问题', 'VI手册缺乏对线上应用的详细指导'], 'adaptation_recommendations': ['建议简化Logo用于社交媒体，保留核心元素以提高识别度', '考虑为线上补充更明亮、清新的辅助色系以增强活力感', '确保字体在数字媒体上的可读性和授权合规', '更新VI手册，增加对线上应用的详细规范和指导']}
    # m1: 现有 Logo、VI 手册等是否适合在数字和社交媒体上传播
    # m1.research_visual_trends( needed_data_for_agent_three.get("./out/Comprehensive_Market_And_Competitor_Intelligence_Report.txt", "Null"))
    
    # m2
    m2(
        needed_data_for_agent_three.get("./out/Brand_Social_Media_Strategic_Playbook.txt", "Null"),
        needed_data_for_agent_three.get("./out/Detailed_Target_Audience_Persona_Portfolie.txt", "Null"),
    )
    
    # 把VISystem单独拎出来
    
    # 生成图片，根据
    
    # KPI生成
    
    
    
    
    
perform_part_three()












































