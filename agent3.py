
from utils import load_file_config, load_files_from_config, output, save_to_file
from agent3_modules.m1_evaluate_existing_visual_assets import research_visual_trends
from agent3_modules.m2_social_VI_system import  m2
from agent3_modules.m3_generate_image import generate_img, generate_main_visual_for_task_prompt
from agent3_modules.m4_kpi import kpi_working
from agent3_modules.Paser import contents_calendar_to_list, JsonToNL, deal_data_for_agent_3
from agent3_modules.m3_out_stragy import refined_distribution_and_engagement_strategy

# m1_out = '''
# 根据提供的品牌战略手册，该品牌的定位为“植物学家闺蜜”，结合科技感、治愈感和环保理念，社交媒体视觉设计趋势应围绕这些核心元素展开。以下是针对当前流行的视觉设计元素、色彩搭配趋势以及排版和布局风格的分析：

# ---

# ### **1. 当前流行的视觉设计元素**
# - **AR交互元素**：  
#   品牌强调“AR扫码溯源植物干细胞”，因此设计中可以融入AR交互的视觉提示，如动态二维码、3D植物生长动画或科技感线条。
  
# - **自然与科技的结合**：  
#   使用植物插画与科技元素（如分子结构、数据可视化）结合，展现“植物学家闺蜜”的双重身份。例如，北极云莓的插画与微囊化科技示意图的结合。

# - **UGC内容展示**：  
#   小红书和抖音平台强调UGC，设计中可以加入真实用户的使用场景（如阳台植物实验室），采用拼贴或蒙太奇风格展示用户生成内容。

# - **环保视觉符号**：  
#   空瓶改造手工课、减碳20%等环保主题需要用视觉符号强化，如再生循环标志、碳足迹图表或自然材质纹理（如木纹、麻布）。

# - **磁吸面膜设计展示**：  
#   通过动态或静态的视觉展示磁吸面膜的使用过程，突出单手操作的便捷性和仪式感。

# ---

# ### **2. 色彩搭配趋势**
# - **主色调**：  
#   - **冷色调为主**：如月光蓝、冰川白、北极云莓的淡紫色，体现科技感和治愈感。  
#   - **自然色调为辅**：如苔藓绿、木质棕，强调植物成分和环保理念。

# - **流行趋势**：  
#   - **渐变透明色**：模拟极光或月光效果，增加科技感和梦幻感。  
#   - **低饱和度色彩**：符合“睡前修复仪式”的舒缓氛围，避免过于刺眼的颜色。  
#   - **对比色点缀**：如深蓝色与金色的搭配（金色象征科技感），提升视觉冲击力。

# ---

# ### **3. 排版和布局风格**
# - **科技感排版**：  
#   - **不对称网格**：打破传统对称布局，体现科技品牌的创新感。  
#   - **数据可视化**：将成分溯源、减碳数据等以图表或信息图形式呈现。  
#   - **极简留白**：突出核心信息，减少视觉干扰。

# - **治愈感排版**：  
#   - **柔和曲线**：使用圆角边框或波浪形分割线，体现“阳台治愈师”的温暖。  
#   - **场景化布局**：如将夜间护肤场景与产品功能结合，营造沉浸式体验。

# - **平台适配**：  
#   - **小红书**：以图文为主，采用高信息密度的拼贴式排版，适合展示UGC和成分分析。  
#   - **抖音**：动态视觉为主，使用快速切换的镜头和字幕强调“通勤急救”或“ASMR仪式”。  
#   - **微信**：长图文或H5设计，适合深度服务内容（如碳积分教程）的层次化展示。

# ---

# ### **总结**
# 品牌的社交媒体视觉设计应围绕“科技+自然+治愈”的核心定位，结合当前流行的AR交互、渐变色彩、不对称布局等趋势，同时根据不同平台的特性调整设计风格。例如：
# - **小红书**：拼贴式UGC展示+成分数据可视化。  
# - **抖音**：动态科技感+场景化治愈内容。  
# - **微信**：极简留白+深度服务信息图。  

# 如果需要更具体的案例或参考，可以进一步搜索相关设计趋势或竞品分析。
# '''

# m2_out = '''
# {'brandVisualIdentitySystem': {'coreDesignConcept': {'description': "融合'植物干细胞科技'的专业性与'月光疗愈'的感性主张，构建兼具实验室精确度与自然疗愈感的品牌识别系统", 'targetAudience': ['成分党理性需求', '环保者情感诉求']}, 'coreVisualElements': {'logoSystem': {'mainLogo': {'description': '双螺旋DNA与北极云莓叶的几何融合，隐藏新月负空间', 'dynamicVersion': {'ARTrigger': '干细胞分裂动画'}}, 'typography': {'fontType': '定制圆角+锐利切割无衬线字体', 'specialCharacter': "'i'字母点替换为分子图标"}}, 'colorSystem': {'techLayer': ['极光蓝(#E6F2FF)', '碳素黑(#1A1A1A)'], 'healingLayer': ['云莓紫(#D8C4F7)', '极地冰蓝(PMS 14-4105TCX)'], 'ecoLayer': ['苔原绿(#5B8C7A)', '苔藓绿(PMS 16-5938TCX)'], 'specialEffects': '月光渐变（蓝→紫→白）应用于动效设计'}, 'dynamicIdentity': {'ARAnimations': ['植物生长动画（含实时碳数据）', '成分可视化粒子动画（如98个光点表98%天然成分）', '磁吸操作动态演示']}}, 'crossPlatformAdaptation': {'platforms': [{'name': '小红书', 'strategy': '实验室笔记风', 'keyElements': ['成分对比卡', '专利文献可视化']}, {'name': '抖音', 'strategy': '科技极光滤镜', 'keyElements': ['磁吸教程GIF', '粒子吸附特效']}, {'name': '微信', 'strategy': '碳积分游戏化', 'keyElements': ['可生长虚拟植物', 'H5交互进度条']}]}, 'ecoInnovationDesign': {'packagingSystem': ['藻类变色油墨（响应光照）', '可拆卸瓶盖DIY盆栽'], 'unboxingExperience': ['月光磁吸盒', '麻纤维内衬', '可种植种子纸'], 'visualSymbols': ['碳足迹循环路径', '显微摄影纹理库']}, 'executionValidation': {'technicalTests': ['眼动仪验证信息布局效率', '色觉障碍用户渐变辨识度测试'], 'experienceMetrics': {'techSenseNPS': '≥7.5', 'ecoLogoRecognitionRate': '≥90%'}}, 'implementationPlan': {'phases': ['优先落地基础系统（核心色+细胞纹理）', '分阶段开发AR组件与平台专属视觉包', '保持微胶囊破裂动画的跨平台一致性'], 'note': '所有设计预留15%空白适配区，确保多媒介兼容性'}}}
# '''

# human_m2_out = '''
# 品牌视觉识别系统的核心设计理念融合了"植物干细胞科技"的专业性与"月光疗愈"的感性主张，旨在构建兼具实验室精确度与自然疗愈感的系统，目标受众包括成分党理性需求和环保者情感诉求。核心视觉元素包括：logo系统的主logo为双螺旋DNA与北极云莓叶的几何融合，隐藏新月负空间，动态版本通过AR触发干细胞分裂动画；字体排版使用定制圆角+锐利切割无衬线字体，其中"i"字母点替换为分子图标；色彩系统分为技术层（如极光蓝#E6F2FF、碳素黑#1A1A1A）、疗愈层（如云莓紫#D8C4F7、极地冰蓝PMS 14-4105TCX）和生态层（如苔原绿#5B8C7A、苔藓绿PMS 16-5938TCX），特殊效果为月光渐变（蓝→紫→白）应用于动效设计；动态识别包括AR动画如植物生长动画（含实时碳数据）、成分可视化粒子动画（如98个光点表98%天然成分）和磁吸操作动态演示。跨平台适配针对小红书采用实验室笔记风策略，关键元素为成分对比卡和专利文献可视化；抖音采用科技极光滤镜策略，关键元素为磁吸教程GIF和粒子吸附特效；微信采用碳积分游戏化策略，关键元素为可生长虚拟植物和H5交互进度条。生态创新设计包括包装系统如藻类变色油墨（响应光照）和可拆卸瓶盖DIY盆栽；开箱体验如月光磁吸盒、麻纤维内衬和可种植种子纸；视觉符号如碳足迹循环路径和显微摄影纹理库。执行验证包括技术测试如眼动仪验证信息布局效率和色觉障碍用户渐变辨识度测试；体验指标要求技术感NPS≥7.5和生态logo识别率≥90%。实施计划分为阶段：优先落地基础系统（核心色+细胞纹理）、分阶段开发AR组件与平台专属视觉包、保持微胶囊破裂动画的跨平台一致性，所有设计预留15%空白适配区确保多媒介兼容性。
# '''

# kpi_out = '''

# ### **KPI扩展表格**

# #### **小红书**
# | **KPI类型**       | **核心KPI**                        | **次核心KPI**                  | **诊断性KPI**                  | **测量方法**                                                                 | **优化建议**                                                                 |
# |-------------------|-----------------------------------|--------------------------------|--------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
# | **认知层**        | 成分溯源直播观看量                | AR互动率                      | 品牌搜索量增长                | 直播观看量统计；AR扫码次数；品牌关键词搜索量监测                              | 提升直播预告频次；优化AR内容互动性                                          |
# | **互动层**        | UGC测评合集互动率（点赞+评论）     | 挑战赛参与人数                | UGC衍生率（KOL:UGC）          | 互动率=（点赞+评论）/观看量；挑战赛参与人数统计；KOL与UGC比例计算             | 设置UGC奖励机制；KOL合作优化                                                |
# | **引导层**        | 点击率 (CTR)                      | 落地页访问量                  | 表单提交数                    | CTR=点击量/曝光量；落地页访问量统计；表单提交数监测                           | 优化文案和视觉；提升落地页加载速度                                          |
# | **品牌健康度**    | 粉丝增长数                        | 品牌声量情感正负比            | 净推荐值 (NPS)                | 粉丝增长数统计；情感分析工具；NPS问卷调查                                    | 加强粉丝互动；负面声量及时回应                                              |

# #### **抖音**
# | **KPI类型**       | **核心KPI**                        | **次核心KPI**                  | **诊断性KPI**                  | **测量方法**                                                                 | **优化建议**                                                                 |
# |-------------------|-----------------------------------|--------------------------------|--------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
# | **认知层**        | #月光疗愈时刻话题播放量           | 通勤急救术视频完播率          | 品牌搜索量增长                | 话题播放量统计；完播率=完整观看量/总观看量；品牌关键词搜索量监测              | 优化话题标签；提升视频前5秒吸引力                                           |
# | **互动层**        | ASMR仪式视频分享率                | 挑战赛参与人数                | 互动率（点赞+评论）           | 分享率=分享量/观看量；挑战赛参与人数统计；互动率=（点赞+评论）/观看量         | 提升ASMR内容沉浸感；设置挑战赛奖励                                          |
# | **引导层**        | 点击率 (CTR)                      | App下载量                     | 表单提交数                    | CTR=点击量/曝光量；App下载量统计；表单提交数监测                              | 优化信息流广告；简化下载流程                                                |
# | **转化层**        | 订单量                            | 销售额                        | ROI                            | 订单量统计；销售额监测；ROI=收入/成本                                        | 优化下单流程；提升产品页面吸引力                                            |

# #### **微信**
# | **KPI类型**       | **核心KPI**                        | **次核心KPI**                  | **诊断性KPI**                  | **测量方法**                                                                 | **优化建议**                                                                 |
# |-------------------|-----------------------------------|--------------------------------|--------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
# | **认知层**        | 碳积分教程阅读量                  | 过敏急速响应通道使用率        | 品牌搜索量增长                | 阅读量统计；使用率=使用人数/总会员数；品牌关键词搜索量监测                    | 优化教程内容；提升响应速度                                                  |
# | **互动层**        | 会员互动率（评论+私信）           | UGC产出数量                   | 互动率（点赞+评论）           | 互动率=（评论+私信）/会员数；UGC数量统计；互动率=（点赞+评论）/阅读量         | 设置会员专属活动；激励UGC产出                                               |
# | **引导层**        | 碳积分激活率                      | 表单提交数                    | App下载量                     | 激活率=激活人数/总会员数；表单提交数监测；App下载量统计                       | 简化激活流程；优化表单设计                                                  |
# | **转化层**        | 会员复购率                        | 销售额                        | ROI                            | 复购率=复购人数/总会员数；销售额监测；ROI=收入/成本                          | 提升会员专属优惠；优化复购提醒                                              |

# ---

# ### **数据分析维度与报告频率**
# 1. **按内容主题**：
#    - 分析不同主题内容的KPI表现（如科技看得见 vs. 仪式治愈力）。
#    - 报告频率：月报。
# 2. **按Persona**：
#    - 分析目标人群的KPI差异（如科技理性派成分党 vs. 环保仪式感追求者）。
#    - 报告频率：季报。
# 3. **按发布时段**：
#    - 分析不同时段的内容表现（如工作日 vs. 周末）。
#    - 报告频率：周报。

# ---

# ### **具体KPI分析**
# 1. **UGC衍生率（小红书）**：
#    - **计算公式**：UGC衍生率 = UGC数量 / KOL发布数量。
#    - **优化建议**：通过挑战赛和奖励机制激励用户生成内容。
# 2. **通勤急救术视频完播率（抖音）**：
#    - **计算公式**：完播率 = 完整观看量 / 总观看量。
#    - **优化建议**：缩短视频时长，提升前5秒吸引力。
# 3. **碳积分激活率（微信）**：
#    - **计算公式**：激活率 = 激活人数 / 总会员数。
#    - **优化建议**：简化激活流程，设置积分奖励。
# '''

# # contents_list = {'tasks': [{'task_name': '月光实验室直播夜', 'task_description': '进行AR直播展示云莓干细胞分裂过程，并包括专家答疑环节。使用小红书直播平台，并创建切片短视频用于传播。', 'time': '1月'}, {'task_name': '#阳台治愈计划', 'task_description': '发起UGC挑战赛鼓励用户晒出自建植物角和月光面膜使用场景，并提供DIY教程指导用户参与。', 'time': '2月'}, {'task_name': '碳足迹可视化面膜', 'task_description': '开发限量版面膜产品，每片包装印上实时减碳数据，并制作开箱视频展示产品特点和环保价值。', 'time': '3月'}, {'task_name': '通勤急救术', 'task_description': '创建磁吸面膜单手操作教程视频，结合场景化测评内容。使用抖音竖屏视频格式，并投放信息流广告推广。', 'time': '4月'}, {'task_name': '成分陪审团', 'task_description': '邀请用户通过私域社群参与新品成分测试活动，并生成署名实验报告分享测试结果和反馈。', 'time': '5月'}, {'task_name': '空瓶改造大师课', 'task_description': '联合艺术家举办线下工作坊和直播课，教导用户如何将空瓶改造为家居艺术品，强调环保再利用。', 'time': '6月'}, {'task_name': '月光疗愈明信片', 'task_description': '制作实体赠品明信片，鼓励用户生成治愈语录，并整合AR植物动画。通过社交媒体互动推广用户参与。', 'time': '7月'}, {'task_name': '植物学家日记', 'task_description': '拍摄原料种植地溯源纪录片，内容涵盖植物生长过程。发布在B站中视频平台，并创建知乎专栏文章补充细节。', 'time': '8月'}, {'task_name': '会员碳积分计划', 'task_description': '实施空瓶回收系统，用户可兑换碳积分换购产品。通过微信小程序管理积分，并发送推送通知提醒用户参与。', 'time': '9月'}, {'task_name': '熬夜肌值夜班', 'task_description': '开发睡前护理ASMR内容，并与睡眠监测APP合作联动。发起抖音挑战赛推广夜间护肤routine。', 'time': '10月'}]}
# contents_list = {
#   "tasks": [
#     {
#       "task_name": "月光实验室直播夜",
#       "task_description": "进行AR直播展示云莓干细胞分裂过程，并包括专家答疑环节。使用小红书直播平台，并创建切片短视频用于传播。",
#       "time": "1月"
#     }
#   ]
# }

# img_prompt = " A high-tech laboratory at night under aurora borealis, moonlight gradient transitions from aurora blue (#E6F2FF) to cloudberry purple (#D8C4F7) to pure white. Central holographic display shows geometric cloudberry stem cells dividing with double helix DNA strands integrated, hidden crescent negative space visible in background glow. Scientific annotations in custom rounded sans-serif with molecular dot icons float like laboratory notes. Petri dish emits soft particle trails in polar ice blue and moss green (#5B8C7A), AR interface elements overlay with transparent carbon black (#1A1A1A) panels. Clean vector plant textures, micro-detail precision, moonlight healing atmosphere, flat design with subtle depth."

def perform_part_three(part_3_input_config='part3_in/in.json', parent_out_path='outputs'):
    # 读取数据
    json_part_3_input = load_file_config(part_3_input_config)
    # output("GREY","input config: {json_part_3_input}")
    needed_data_for_agent_three = load_files_from_config(json_part_3_input)
    # output("GREY", f"{needed_data_for_agent_three}\n\n\n")

    dealed_data_for_agent_3 = deal_data_for_agent_3(needed_data_for_agent_three)
    output("GREY", f"{dealed_data_for_agent_3}")
    
    output("GREY", "m1 start")
    m1_out = research_visual_trends(
        dealed_data_for_agent_3.get("Brand_Social_Media_Strategic_Playbook", "no info here"),
    )
    output("BLACK", f"m1的输出: \n{m1_out}")
    output("GREY", "QED m1 -----------------------------")
    
    output("GREY", "m2 start")
    m2_out = m2(
        brand_info=dealed_data_for_agent_3.get("Brand_Social_Media_Strategic_Playbook", "no info here"),
        target_audience=dealed_data_for_agent_3.get("Detailed_Target_Audience_Persona_Portfolio", "no info here"),
        _trend_analyze=m1_out
    )
    output("BLACK", f"m2的输出: {m2_out}")
    output("GREY", "human_m2 start")
    human_vi = JsonToNL(m2_out)
    save_to_file(f"{human_vi}", parent_out_path, "Social_Media_Visual_Identity_System_Guide.md")
    output("BLACK", f"{human_vi}")
    output("GREY", "human_m2 end")
    
    
    # KPI生成
    output("GREY", "kpi start")
    kpi = kpi_working(
        brand_and_simple_kpi=dealed_data_for_agent_3.get("Brand_Social_Media_Strategic_Playbook", "no info here"),
        content_calendar=dealed_data_for_agent_3.get("Content_Idea_Repository", "no info here"),
    )
    output("BLACK", f"KPI的输出：{kpi} ")
    save_to_file(kpi, parent_out_path, "Comprehensive_KPI_Framework_And_Reporting_Template.md")
    output("GREY", "kpi end")
    
    
    
    # 生成图片，根据内容日历
    output("GREY", "contents_calendar_to_list start")
    contents_list = contents_calendar_to_list(
        dealed_data_for_agent_3.get("Content_Idea_Repository", "no info here"),
    )
    output("BLACK", f"Info contents_list: {contents_list}")
    output("GREY", "contents_calendar_to_list end")
    for single_task in contents_list.get('tasks', []):
        human_input = input("是否继续(输入y表示继续生成, 其余字符表示不继续):")
        if human_input != 'y':
          break
        output("GREEN", f"{single_task}")
          
        # 精细化发布策略
        output("GREY", "精细化发布策略 start")
        more_out_info = refined_distribution_and_engagement_strategy(
            task=f"Info single_task: {single_task}",
            trend_info=m1_out,
            brand_story=dealed_data_for_agent_3.get("Brand_Social_Media_Strategic_Playbook", "no info here"),
            audience_info=dealed_data_for_agent_3.get("Detailed_Target_Audience_Persona_Portfolio", "no info here")
        )
        save_to_file(f"{more_out_info}", parent_out_path, single_task.get('task_name', "tmp_res"), parent_out_path+single_task.get('task_name', "tmp_res") + ".md")
        output("GREY", "精细化发布策略 end")
        
        # 主视觉生成
        output("GREY", "img start")
        img_prompt = generate_main_visual_for_task_prompt(single_task, vi_system=m2_out)
        # output("GREY", f"生成图片提示词: {img_prompt}")
        generate_img(img_prompt=img_prompt, output_name=single_task.get('task_name', "tmp_res"), parent_path=parent_out_path )
        output("GREY", "img end")
          
