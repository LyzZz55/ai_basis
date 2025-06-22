

import sys
from pathlib import Path
# 获取项目根目录并添加到sys.path
project_root = str(Path(__file__).parent.parent.parent)  # 根据实际结构调整
sys.path.append(project_root)
# 使用绝对导入
from part_3.utils import load_file_config, load_files_from_config
from part_3.modules.m1_evaluate_existing_visual_assets import BrandVisualAnalyzer


def perform_part_three():
    
    # 读取数据
    json_part_3_input = load_file_config("./out/part_3_in.json")
    print(json_part_3_input)
    
    # M 1
    # m1 = BrandVisualAnalyzer()
    # 评估现有 Logo、VI 手册等是否与 Agent 1 定义的品牌“人设”和“语调”匹配
    # m1: 现有 Logo、VI 手册等是否适合在数字和社交媒体上传播
    
    
perform_part_three()












































