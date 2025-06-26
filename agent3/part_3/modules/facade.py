
import sys
from pathlib import Path
# 获取项目根目录并添加到sys.path
project_root = str(Path(__file__).parent.parent.parent)  # 根据实际结构调整
sys.path.append(project_root)
# 使用绝对导入
from part_3.utils import load_file_config, load_files_from_config, output, save_to_file
from part_3.modules.m1_evaluate_existing_visual_assets import research_visual_trends
from part_3.modules.m2_social_VI_system import  m2
from part_3.modules.m3_generate_image import generate_img, generate_main_visual_for_task_prompt
from part_3.modules.m4_kpi import kpi_working
from part_3.modules.Paser import contents_calendar_to_list, JsonToNL
from part_3.modules.m3_out_stragy import refined_distribution_and_engagement_strategy


m1_out = """
### **1. 当前流行的视觉设计元素**
#### **趋势分析**
- **自然与科技结合**：  
  行业趋势显示，技术民主化和环保实证主义是核心方向。设计上需体现“自然与科技”的融合，例如：
  - **植物干细胞可视化**：用微距摄影或3D动画展示植物干细胞，结合生活化比喻（如“缓释小水弹”）。
  - **AR/VR元素**：AR碳足迹追踪功能可设计为动态图标或交互式视觉标签（如扫描包装后显示动态供应链路线）。

- **极简主义与有机感**：  
  天然有机护肤品行业偏向极简设计，但需加入有机纹理（如叶脉、水滴）增强亲和力。

#### **品牌应用**
- **动态内容**：  
  - 抖音：3秒技术动画（如“从实验室到肌肤”的极简流程）。
  - 小红书：成分溯源直播的背景设计可加入动态植物生长效果。
- **UGC激励**：  
  鼓励用户分享带有品牌标志性元素（如绿叶图标、碳足迹标签）的创意内容。

---

### **2. 色彩搭配趋势**
#### **趋势分析**
- **自然色系主导**：  
  - **核心色**：柔和的绿色（象征自然）、大地色（如米白、浅棕）和低饱和度蓝色（象征科技与纯净）。
  - **点缀色**：亮绿色或金色（用于突出技术感和高级感）。

- **环保主题色**：  
  行业趋势显示碳足迹可视化是重点，可加入“碳中性灰”或“生态蓝”作为辅助色。

#### **品牌应用**
- **平台差异化**：  
  - **抖音**：高对比度色彩（如亮绿+白）吸引眼球。
  - **小红书**：柔和的自然色系（如薄荷绿+米白）增强信任感。
  - **Instagram**：使用统一的滤镜（如低饱和度+自然光）保持品牌一致性。

---

### **3. 排版和布局风格**
#### **趋势分析**
- **不对称与留白**：  
  现代设计偏向非对称布局，搭配大量留白以突出核心信息（如成分透明化、碳足迹数据）。

- **模块化设计**：  
  适合跨平台叙事（如抖音→小红书→私域），将内容拆分为可复用的模块（如技术卡片、用户见证板块）。

#### **品牌应用**
- **信息分层**：  
  - **屋顶标语**：大字号居中排版，搭配极简背景（如纯色或微距植物纹理）。
  - **三大支柱**：用图标+短文案的卡片式设计，便于用户快速理解。
- **平台适配**：  
  - **抖音**：单屏聚焦（如左图右文，或全屏动画）。
  - **小红书**：长图文结合，突出UGC内容（如用户测评的网格布局）。

---

### **总结建议**
1. **视觉元素**：结合动态科技感与自然纹理，强化AR/VR互动设计。
2. **色彩**：以自然色系为主，平台差异化调整饱和度。
3. **排版**：模块化+留白，适配各平台内容需求（如抖音快闪 vs. 小红书深度）。
"""

m2_out=\
{'brandName': 'EcoGarden', 'brandSlogan': None, 'coreValues': ['科技自然', '透明可信', '简约高效'], 'coreElements': ['植物干细胞', '可持续发展'], 'logo': {'description': '抽象化的植物叶脉或细胞结构与几何线条或科技元素相结合，简洁现代', 'mainColor': '#a7d1ab', 'secondaryColors': ['#f5f5dc', '#d3d3d3', '#808080', '亮绿色', '金色'], 'font': {'primary': '现代感强、易读性高的无衬线字体', 'secondary': '衬线字体'}, 'variations': ['不同尺寸', '不同版本', '动画版本']}, 'colorPalette': {'mainColor': '#a7d1ab', 'secondaryColors': ['#f5f5dc', '#d3d3d3', '#808080'], 'accentColors': ['亮绿色', '金色'], 'platformAdjustment': '根据平台差异，适度调整色彩饱和度和亮度'}, 'layoutSystem': {'designPrinciple': '模块化设计，例如成分卡片、技术卡片、环保数据卡片等', 'whitespace': '充分利用留白，清晰划分信息层级，确保易读性和视觉舒适度'}, 'platformStrategies': {'Douyin': '强调动感和视觉冲击', 'Xiaohongshu': '注重生活化和用户生成内容', 'Instagram': '保持高度视觉一致性'}, 'ARVRApplications': {'AR': '产品成分溯源和碳足迹追踪的可视化', 'VR': '微距摄影或3D动画展现植物干细胞的科技感'}, 'userExperience': {'principles': ['易用性', '一致性', '可访问性'], 'testing': '建议进行用户测试以确保设计方案的有效性'}, 'iteration': '持续关注市场趋势，并根据用户反馈不断迭代优化VI系统，确保其长期有效性'}


kpi = """

### **EcoGarden有机护肤KPI细化框架**

#### **1. 抖音平台**
| **营销目标**          | **核心KPI**       | **次核心KPI**       | **诊断性KPI**       | **目标值**       |
|-----------------------|------------------|---------------------|---------------------|-----------------|
| 月光面膜认知度40%     | 视频完播率       | 曝光量              | 3秒播放率           | ≥65%            |
| 会员注册转化          | CTR (点击率)     | 落地页访问量        | 跳出率              | 7.2%            |
| 新品引爆效果          | 分享率           | 评论互动率          | 粉丝增长数          | ≥5%             |

**分析维度**：
- 按内容主题：技术动画 vs. 会员钩子
- 按发布时段：工作日 vs. 周末
- 按用户画像：新用户 vs. 老用户  
**报告频率**：周报

---

#### **2. 小红书平台**
| **营销目标**          | **核心KPI**       | **次核心KPI**       | **诊断性KPI**       | **目标值**       |
|-----------------------|------------------|---------------------|---------------------|-----------------|
| UGC 10,000+           | UGC投稿量/周     | 互动率              | UGC质量评分         | 800篇           |
| 信任基建效果          | 直播观看时长     | 直播互动率          | 品牌搜索量增长      | ≥15分钟         |
| 环保挑战参与度        | 挑战话题参与量   | 分享率              | 情感正负比          | ≥1,000次        |

**分析维度**：
- 按内容主题：成分溯源 vs. 环保挑战
- 按用户行为：直播观众 vs. 话题参与者  
**报告频率**：周报

---

#### **3. 全域平台**
| **营销目标**          | **核心KPI**       | **次核心KPI**       | **诊断性KPI**       | **目标值**       |
|-----------------------|------------------|---------------------|---------------------|-----------------|
| 新增会员5,000人       | 会员转化率       | 注册表单提交数      | 渠道来源分布        | 7.2%            |
| 跨平台ROI≥1:2.5       | ROI              | 客单价              | 用户旅程路径分析    | 1:2.5           |
| 品牌健康度            | NPS (净推荐值)   | 粉丝增长数          | 品牌声量情感正负比  | ≥40             |

**分析维度**：
- 按渠道：抖音 vs. 小红书 vs. 私域
- 按用户生命周期：新用户 vs. 复购用户  
**报告频率**：月报

---

#### **4. 私域平台**
| **营销目标**          | **核心KPI**       | **次核心KPI**       | **诊断性KPI**       | **目标值**       |
|-----------------------|------------------|---------------------|---------------------|-----------------|
| 会员复购率35%         | 90天复购频次     | 复购客单价          | 会员活跃度          | ≥2.1次          |
| 碳积分系统效果        | 积分兑换率       | 会员留存率          | 碳足迹追踪参与度    | ≥30%            |
| 品牌忠诚度            | 私域互动率       | 社群活跃度          | UGC产出量           | ≥10%            |

**分析维度**：
- 按会员等级：普通会员 vs. 高级会员
- 按活动类型：碳积分 vs. 新品首发  
**报告频率**：月报

---

### **详细KPI分析**

#### **1. 视频完播率（抖音）**
- **测量方法**：播放完成次数 / 播放总次数
- **计算公式**：完播率 = (播放完成数 ÷ 播放总数) × 100%
- **优化建议**：
  - 调整视频前3秒吸引用户注意力。
  - 测试不同视频长度（如15秒 vs. 30秒）。

#### **2. UGC投稿量（小红书）**
- **测量方法**：统计每周新增UGC帖子的数量。
- **计算公式**：UGC投稿量 = 每周新增帖子数
- **优化建议**：
  - 提供UGC激励计划（如抽奖、曝光机会）。
  - 优化话题标签设计，提高用户参与意愿。

#### **3. 会员复购频次（私域）**
- **测量方法**：统计会员在90天内购买的次数。
- **计算公式**：复购频次 = 总复购次数 ÷ 会员总数
- **优化建议**：
  - 定期推送个性化优惠。
  - 设计会员专属活动（如新品优先购）。

#### **4. 跨平台ROI**
- **测量方法**：总收入 ÷ 总广告支出
- **计算公式**：ROI = (收入 ÷ 成本) × 100%
- **优化建议**：
  - 优化用户旅程路径（如抖音引流 → 小红书验真 → 私域复购）。
  - 分析高ROI渠道，增加投放预算。

---

### **KPI关联性分析**
- **认知层 → 互动层**：高完播率（抖音）可能带动UGC投稿量（小红书）。
- **互动层 → 转化层**：UGC质量评分（小红书）可能影响会员转化率（全域）。
- **转化层 → 品牌健康度**：高复购频次（私域）可能提升NPS（全域）。
"""

contents_list = {'tasks': [{'task_name': '7月抖音干细胞科普动画制作', 'task_description': "制作30秒动画《5步看懂干细胞变护肤品》，配'微囊不是魔法，是慢释放小水弹'标语，植入会员注册入口，目标完播率≥65%", 'platform': '抖音', 'time': '7月2日', 'theme': '植物干细胞科普周'}, {'task_name': '7月小红书博士IP直播', 'task_description': '李媛博士IP直播《从实验室到面膜的成分溯源》，现场演示干细胞萃取实验，同步发起#成分透明挑战#，目标UGC周增800篇', 'platform': '小红书', 'time': '7月3日', 'theme': '植物干细胞科普周'}, {'task_name': '8月全平台AR碳足迹视频', 'task_description': '陈雅（环保先锋人设）开箱视频《一片面膜的碳中和之旅》，演示AR扫描包装显示供应链碳足迹，发起#我的碳积分挑战#', 'platform': '全平台', 'time': '8月1日', 'theme': 'AR碳足迹上线周'}, {'task_name': '8月私域碳积分系统上线', 'task_description': '碳积分系统上线（1积分=1g减碳量），会员可兑换生态摄影集，同步提升复购频次至1.7次/90天', 'platform': '私域', 'time': '8月1日', 'theme': 'AR碳足迹上线周'}, {'task_name': '9月抖音新品技术动画', 'task_description': "3秒技术动画《新一代配方3大升级点》+限时折扣，直接拉动'月光面膜'认知度达40%", 'platform': '抖音', 'time': '9月1日', 'theme': '新品首发周'}, {'task_name': '9月小红书配方师直播', 'task_description': '配方师Gigi直播《成分党必看的新品对比测评》，同步开放会员优先购通道，缩短决策周期至2.4周', 'platform': '小红书', 'time': '9月1日', 'theme': '新品首发周'}]}


def perform_part_three(need_sace=True, parent_out_path='3_out'):
    
    # 读取数据
    json_part_3_input = load_file_config("3_input_files/part_3_in.json") # TODO 不要写死
    output("BLACK","input config: {json_part_3_input}", None, False)
    needed_data_for_agent_three = load_files_from_config(json_part_3_input)
    output("BLACK", f"data for agent3 {needed_data_for_agent_three}", None, False)

    m1_out = research_visual_trends(
        needed_data_for_agent_three.get("3_input_files/2_brand_story.txt", "no brand story now"),
        needed_data_for_agent_three.get("3_input_files/4_industry_trends.txt", "no industry trends now"),
    )
    output("BLACK", f"m1的输出: {m1_out}", None, False)
    output("BLACK", "QED-----------------------------", None, False)
    
    m2_out = m2(
        needed_data_for_agent_three.get("3_input_files/2_brand_story.txt", "Null"),
        needed_data_for_agent_three.get("3_input_files/5_audience_personas.txt", "Null"),
        trend_analyze=m1_out
    )
    output("BLACK", f"m2的输出: {m2_out}", None, False)
    human_vi = JsonToNL(m2_out)
    save_to_file(f"{human_vi}", parent_out_path, "Social_Media_Visual_Identity_System_Guide.md")
    
    
    # KPI生成
    kpi = kpi_working(
        needed_data_for_agent_three.get("3_input_files/7_kpi.txt", "Null"),
        needed_data_for_agent_three.get("3_input_files/2_brand_story.txt", "Null"),
        needed_data_for_agent_three.get("3_input_files/6_content_calendar.txt", "Null"),
    )
    output("BLACK", f"KPI的输出：{kpi} ", None, False)
    save_to_file(kpi, parent_out_path, "Comprehensive_KPI_Framework_And_Reporting_Template.md")
    
    
    
    # 生成图片，根据内容日历
    contents_list = contents_calendar_to_list(
        needed_data_for_agent_three.get("3_input_files/6_content_calendar.txt", "Null"),
    )
    output("BLACK", f"Info contents_list: {contents_list}", None, False)
    
    for single_task in contents_list.get('tasks', []):
        output("BLACK", f"Info single_task: {single_task}", None, False)
      
        # 精细化发布策略
        more_kpi_info = refined_distribution_and_engagement_strategy(
          f"Info single_task: {single_task}",
          needed_data_for_agent_three.get("3_input_files/4_industry_trends.txt", "no industry trends now"),
          needed_data_for_agent_three.get("3_input_files/2_brand_story.txt", "Null"),
          needed_data_for_agent_three.get("3_input_files/5_audience_personas.txt", "Null"),
        )
        save_to_file(more_kpi_info, parent_out_path, single_task.get('task_name', "tmp_res"), parent_out_path+single_task.get('task_name', "tmp_res") + ".md")
        
        
        # 主视觉生成
        img_prompt = generate_main_visual_for_task_prompt(single_task, vi_system=m2_out)
        output("BLACK", f"Info 生成图片提示词: {img_prompt}", None, False)
        
        generate_img(vi_system=m2_out, img_requirement=img_prompt, output_path=parent_out_path + single_task.get('task_name', "tmp_res")+ "/" + single_task.get('task_name', "tmp_res") )
        
    
perform_part_three()

