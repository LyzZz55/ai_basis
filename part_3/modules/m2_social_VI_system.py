########################################################################################
# + VI系统构建:
#       构建详细的社交媒体视觉识别系统，包括色彩、字体、图像风格
# + 视觉模板概念设计:
#       适用场景、布局草图描述、VI应用说明等
# + 生成设计规范文档
########################################################################################

from dotenv import load_dotenv
import os
import json
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

import sys
from pathlib import Path
# 获取项目根目录并添加到sys.path
project_root = str(Path(__file__).parent.parent.parent)  # 根据实际结构调整
sys.path.append(project_root)
# 使用绝对导入
from part_3.utils import clean_json_string

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")


class SocialVISystem:
    def __init__(self):
        """初始化社交媒体VI系统构建器，创建AI模型和代理"""
        self.dpsk = ModelFactory.create(
            model_platform=ModelPlatformType.SILICONFLOW,
            model_type='Pro/deepseek-ai/DeepSeek-V3',
            model_config_dict={
                "max_tokens": 4096,
                "temperature": 0.7
            },
            api_key=SF_API_KEY,
        )
        self.gemini = ModelFactory.create(
            model_platform=ModelPlatformType.GEMINI,
            model_type=ModelType.GEMINI_2_0_FLASH,
            model_config_dict={
                "max_tokens": 4096,
                "temperature": 0.7
            },
            api_key=GEMINI_API_KEY,
        )
        
        # 初始化各模块代理（使用动态生成的Prompt）
        self.color_palette_agent = ChatAgent(
            system_message=self._get_color_palette_prompt(),
            model=self.gemini,
            message_window_size=1000,
        )
        self.image_style_agent = ChatAgent(
            system_message=self._get_image_style_prompt(),
            model=self.gemini,
            message_window_size=1000,
        )
        self.typography_agent = ChatAgent(
            system_message=self._get_typography_prompt(),
            model=self.dpsk,
            message_window_size=1000,
        )
        self.layout_agent = ChatAgent(
            system_message=self._get_layout_prompt(),
            model=self.dpsk,
            message_window_size=1000,
        )
        self.trend_analysis_agent = ChatAgent(
            system_message=self._get_trend_analysis_prompt(),
            model=self.gemini,
            message_window_size=1000,
        )
    
    def _get_color_palette_prompt(self) -> str:
        """生成色彩体系设计Prompt（专业品牌视觉设计规范）"""
        return """
        你是具有10年以上经验的品牌视觉设计专家，擅长为社交媒体场景定制色彩体系。请根据输入生成符合以下要求的品牌色彩系统：
        
        输出必须为严格JSON格式，结构如下：
        {
            "primary_colors": "品牌核心识别色（1-2种），格式为HEX值数组，如['#0070F3', '#FF6B00']",
            "secondary_colors": "辅助支持色（2-3种），用于扩展主色的视觉表达",
            "accent_colors": "交互强调色（1-2种），用于按钮、图标等交互元素",
            "neutral_colors": "中性基础色（文本/背景），包含黑、白、灰系列",
            "psychology_notes": "色彩心理学效应分析，说明每种主色传递的情感和认知",
            "social_media_adaptation": "针对社交媒体场景的适配说明，如小屏幕显示优化、色彩对比度建议"
        }
        
        输入参数将包含：
        1. 现有品牌主色（如有）
        2. 品牌语调关键词（如'科技感'、'亲和力'）
        3. 目标受众视觉偏好
        4. 行业色彩趋势分析
        5. 视觉设计原则知识库
        
        要求：
        - 色彩体系需符合社交媒体平台的显示特性（如屏幕色域、亮度环境）
        - 主色需与品牌核心价值高度关联，辅助色需与主色形成和谐搭配
        - 强调色需满足WCAG对比度标准，确保可读性
        - 中性色需覆盖文本、背景、边框等不同场景应用
        """
    
    def _get_image_style_prompt(self) -> str:
        """生成图像风格指南Prompt（全媒体视觉一致性规范）"""
        return """
        你是资深品牌视觉设计师，专注于社交媒体图像风格体系构建。请根据输入生成完整的品牌图像风格指南，输出必须为严格JSON格式：
        
        {
            "photography_style": {
                "overall_mood": "摄影作品的整体情感基调（如'温暖治愈'、'科技未来'）",
                "subject_matter": "拍摄主体选择原则（如'真实生活场景'、'产品特写'）",
                "composition_rules": "构图法则（如'三分法'、'中心构图'）",
                "color_palette_reference": "与品牌色彩体系的映射关系",
                "lighting_guidelines": "光线运用原则（如'自然光优先'、'高对比度打光'）",
                "dos_examples": ["符合风格的示例描述"],
                "donts_examples": ["需避免的示例描述"]
            },
            "illustration_graphic_style": {
                "primary_style": "核心插画风格（如'扁平化'、'手绘质感'、'3D渲染'）",
                "iconography_system": "图标设计规范（如'线性图标'、'填充图标'）",
                "data_visualization_style": "数据可视化呈现方式",
                "color_application": "品牌色彩在图像中的具体应用规则",
                "usage_scenarios": "不同风格元素的适用场景说明"
            },
            "video_style_guide": {
                "visual_rhythm": "视频视觉节奏描述（如'快速切换'、'缓慢叙事'）",
                "motion_guidelines": "动态效果原则（如'平滑过渡'、'弹性动画'）",
                "branding_elements": "品牌标识在视频中的呈现规范"
            }
        }
        
        输入将包含品牌语调关键词、受众视觉偏好、行业视觉趋势等信息，
        要求输出内容必须与品牌核心价值高度一致，并符合社交媒体平台的视觉传播特性。
        """
    
    def _get_typography_prompt(self) -> str:
        """生成字体系统设计Prompt（跨平台排版规范）"""
        return """
        你是专业的排版设计师，擅长为品牌构建跨平台字体系统。请根据输入生成适合社交媒体场景的字体体系，输出为严格JSON格式：
        
        {
            "primary_headline_font": {
                "family": "主标题字体家族（如'Inter'、'思源黑体'）",
                "weights": ["字体字重列表（如'400', '600', '700'）"],
                "style_description": "字体风格描述（如'现代无衬线'、'优雅衬线'）",
                "usage_scenarios": "适用场景说明（如'社交媒体帖子标题'、'广告横幅'）"
            },
            "secondary_headline_font": {
                "family": "次标题字体家族",
                "weights": ["字体字重列表"],
                "style_description": "字体风格描述",
                "complementarity_notes": "与主标题字体的搭配说明"
            },
            "body_text_font": {
                "family": "正文文本字体家族",
                "weights": ["字体字重列表"],
                "style_description": "字体风格描述（如'易读性优先'）",
                "readability_optimizations": "针对小屏幕的可读性优化措施"
            },
            "typographic_scale": [
                {
                    "element": "排版元素名称（如'帖子标题'、'正文'、'注释'）",
                    "font_family": "字体家族引用",
                    "size_desktop": "桌面端字号",
                    "size_mobile": "移动端字号",
                    "weight": "字重",
                    "line_height": "行高"
                }
            ],
            "multilanguage_support": "多语言支持说明（如'支持中日韩字符集'）",
            "licensing_guide": "字体授权使用建议",
            "social_media_adaptation": "社交媒体场景下的特殊排版规则（如'标签文本样式'、'评论区字体规范'）"
        }
        
        输入将包含现有字体、品牌人设关键词、多语言需求等信息，
        要求输出字体系统需同时满足视觉表现力和跨平台可读性。
        """
    
    def _get_layout_prompt(self) -> str:
        """生成版式设计Prompt（视觉层次与空间规范）"""
        return """
        你是视觉布局专家，擅长创建符合品牌调性的社交媒体版式系统。请根据输入生成完整的布局与构图原则，输出为JSON格式：
        
        {
            "grid_system": {
                "base_unit": "基础网格单位（如'8px'）",
                "column_count": "网格列数",
                "gutter_width": "列间距",
                "social_media_adaptations": "各社交平台网格适配规则（如'Instagram方形构图'）"
            },
            "whitespace_strategy": {
                "main_content_padding": "主内容区留白标准",
                "visual_breathing_space": "元素间留白原则",
                "importance_of_whitespace": "留白对品牌信息传达的影响说明"
            },
            "visual_hierarchy": {
                "hierarchy_rules": "信息层级划分原则（如'字号差1.5倍'、'色彩对比度区分'）",
                "key_elements_priority": "关键元素优先级排序（如'Logo>标题>正文'）",
                "social_media_attention_rules": "社交媒体场景下的注意力引导策略"
            },
            "brand_elements_placement": {
                "logo_placement": "Logo位置规范（如'左上角固定'、'底部居中'）",
                "logo_clear_space": "Logo周围留白标准",
                "watermark_strategy": "品牌水印添加原则"
            },
            "cross_platform_adaptation": {
                "desktop_layout": "桌面端布局要点",
                "mobile_layout": "移动端布局要点",
                "special_platforms": "特殊平台适配说明（如'故事模式'、'直播界面'）"
            }
        }
        
        输入将包含品牌色彩系统、字体系统和视觉设计原则，
        要求输出布局方案需强化品牌识别度并提升社交媒体内容的传播效果。
        """
    
    def _get_trend_analysis_prompt(self) -> str:
        """生成趋势分析Prompt（行业视觉趋势洞察）"""
        return """
        你是市场趋势分析专家，专注于社交媒体视觉设计趋势研究。请根据输入生成行业视觉趋势分析报告，输出为JSON格式：
        
        {
            "current_industry_trends": [
                {
                    "trend_name": "趋势名称",
                    "color_characteristics": "色彩特征描述",
                    "design_elements": "设计元素特点",
                    "popularity_index": "流行度指数（1-10）",
                    "social_media_applications": "在社交媒体中的应用场景"
                }
            ],
            "audience_preference_analysis": {
                "color_preferences": "目标受众色彩偏好分析",
                "style_preferences": "风格偏好分析",
                "engagement_characteristics": "高参与度内容的视觉特征"
            },
            "competitor_visual_strategies": [
                {
                    "competitor_name": "竞争对手名称",
                    "color_strategy": "色彩策略分析",
                    "visual_style": "视觉风格总结",
                    "social_media_performance": "社交媒体表现分析"
                }
            ],
            "trend_recommendation": {
                "suitable_trends": "适合品牌采用的趋势列表",
                "trend_adaptation_strategies": "趋势适配策略",
                "differentiation_opportunities": "差异化机会点"
            }
        }
        
        输入将包含品牌行业、目标受众画像、竞争对手分析等信息，
        要求输出内容具有前瞻性和可操作性，能够为品牌视觉设计提供方向指导。
        """
    
    # ------------------------- 核心功能方法 -------------------------
    def _define_color_palette(
        self,
        existing_colors_str: str,
        brand_tone_descriptors_str: str,
        audience_visual_preferences_str: str,
        industry_trends_data: list,
        visual_design_principles_kb: dict
    ) -> dict:
        """生成品牌色彩体系（使用动态Prompt）"""
        print("  模块3.1: 生成色彩体系...")
        usr_msg = f"""
        现有品牌主色: {existing_colors_str}
        品牌语调描述: {brand_tone_descriptors_str}
        受众视觉偏好: {audience_visual_preferences_str}
        行业趋势色彩: {industry_trends_data}
        设计原则知识: {visual_design_principles_kb}
        """
        try:
            response = self.color_palette_agent.step(usr_msg)
            str_res = response.msgs[0].content
            clean_res = clean_json_string(str_res)
            return json.loads(clean_res)
        except json.JSONDecodeError as e:
            print(f"[色彩体系] JSON解析错误: {e}")
            return {"error": f"JSON解析失败: {str_res}"}
        except Exception as e:
            print(f"[色彩体系] AI调用异常: {e}")
            return {"error": str(e)}
    
    def _define_typography_system(
        self,
        existing_fonts_str: str,
        brand_playbook_data: dict,
        multi_language_needed: bool = False
    ) -> dict:
        """生成品牌字体系统（使用动态Prompt）"""
        print("  模块3.2: 生成字体系统...")
        persona_keywords = brand_playbook_data.get('brand_persona_keywords_list_str', '[]')
        tone_keywords = brand_playbook_data.get('brand_tone_descriptors_list_str', '[]')
        
        agent = ChatAgent(
            system_message=self._get_typography_prompt(),
            model=self.dpsk,
            message_window_size=1000,
        )
        usr_msg = f"""
        现有品牌字体: {existing_fonts_str}
        品牌人设关键词: {persona_keywords}
        品牌语调关键词: {tone_keywords}
        多语言支持需求: {"需要" if multi_language_needed else "不需要"}
        """
        try:
            response = agent.step(usr_msg)
            str_res = response.msgs[0].content
            clean_res = clean_json_string(str_res)
            return json.loads(clean_res)
        except json.JSONDecodeError as e:
            return {"error": f"字体系统JSON解析错误: {e}", "raw": str_res}
        except Exception as e:
            return {"error": f"字体系统AI调用异常: {e}"}
    
    def _define_imagery_style_guide(
        self,
        brand_playbook_data: dict,
        audience_persona_data: dict,
        trend_research_output: dict
    ) -> dict:
        """生成品牌图像风格指南（使用动态Prompt）"""
        print("  模块3.3: 生成图像风格指南...")
        tone_keywords = brand_playbook_data.get('brand_tone_descriptors_list_str', '[]')
        audience_keywords = audience_persona_data.get('visual_preferences_keywords_list_str', '[]')
        industry_trends = trend_research_output.get('current_industry_trends', [])
        
        usr_msg = f"""
        品牌语调关键词: {tone_keywords}
        受众视觉偏好: {audience_keywords}
        行业视觉趋势: {industry_trends}
        """
        try:
            response = self.image_style_agent.step(usr_msg)
            str_res = response.msgs[0].content
            clean_res = clean_json_string(str_res)
            return json.loads(clean_res)
        except json.JSONDecodeError as e:
            print(f"[图像风格] JSON解析错误: {e}")
            return {"error": f"图像风格JSON解析失败: {str_res}"}
        except Exception as e:
            print(f"[图像风格] AI调用异常: {e}")
            return {"error": str(e)}
    
    def _define_video_style_guide(
        self,
        brand_playbook_data: dict,
        audience_persona_data: dict,
        trend_research_output: dict
    ) -> dict:
        """生成品牌视频风格指南"""
        print("  模块3.4: 生成视频风格指南...")
        tone_keywords = brand_playbook_data.get('brand_tone_descriptors_list_str', '[]')
        audience_video_preferences = audience_persona_data.get('video_preferences_keywords_list_str', '[]')
        video_trends = trend_research_output.get('current_industry_trends', [])
        
        # 调用趋势分析代理获取视频趋势洞察
        trend_analysis = self.trend_analysis_agent.step(f"分析视频视觉趋势: {video_trends}")
        trend_insights = json.loads(clean_json_string(trend_analysis.msgs[0].content))
        
        return {
            "video_mood": f"结合{tone_keywords}的品牌调性，采用{audience_video_preferences}的受众偏好元素",
            "visual_elements": f"融入{[trend['trend_name'] for trend in trend_insights.get('suitable_trends', [])]}",
            "motion_guidelines": "遵循平滑过渡与品牌节奏的动态效果原则",
            "branding_placements": "品牌标识在视频中的固定位置与曝光频率规范"
        }
    
    def _define_layout_principles(
        self,
        color_system: dict,
        typography_system: dict,
        visual_design_principles_kb: dict
    ) -> dict:
        """生成版式与构图原则（结合动态Prompt与AI生成）"""
        print("  模块3.5: 生成版式与构图原则...")
        # 提取关键信息用于布局设计
        primary_color = color_system.get('primary_colors', ['#000'])[0]
        headline_font = typography_system.get('primary_headline_font', {}).get('family', '无衬线字体')
        
        # 调用布局代理生成专业布局方案
        usr_msg = f"""
        品牌主色: {primary_color}
        标题字体: {headline_font}
        设计原则: {visual_design_principles_kb}
        """
        try:
            response = self.layout_agent.step(usr_msg)
            str_res = response.msgs[0].content
            clean_res = clean_json_string(str_res)
            return json.loads(clean_res)
        except Exception as e:
            print(f"[版式设计] AI调用异常: {e}")
            return {
                "grid_system": "建议采用8点栅格系统保证跨平台一致性",
                "whitespace_usage": "主内容区保留30%留白增强可读性",
                "visual_hierarchy": f"使用{primary_color}作为强调色，标题使用{headline_font}字体"
            }
    
    def build_social_vi_system(
        self,
        brand_visual_assets_data: dict,
        brand_playbook_data: dict,
        target_audience_persona_data: dict,
        module1_asset_analysis_output: dict,
        module2_trend_research_output: dict
    ) -> dict:
        """构建完整社交媒体VI系统"""
        print("模块3: 开始构建社交媒体视觉识别系统...")
        visual_design_principles_kb = {
            "color_psychology": {"blue": "科技、信任", "green": "自然、健康"},
            "layout_theory": {"grid": "8点系统", "hierarchy": "字号差1.5倍"},
            "typography_rules": {"line_height": "1.5-1.8"}
        }  # 实际应从知识库加载
        
        # 调用各子模块生成VI组件
        color_system = self._define_color_palette(
            brand_visual_assets_data.get("existing_colors_list_str", "[]"),
            brand_playbook_data.get("brand_tone_descriptors_list_str", "[]"),
            target_audience_persona_data.get("visual_preferences_keywords_list_str", "[]"),
            module2_trend_research_output.get("color_trends", []),
            visual_design_principles_kb
        )
        typography_system = self._define_typography_system(
            brand_visual_assets_data.get("existing_fonts_list_str", "[]"),
            brand_playbook_data,
            brand_playbook_data.get("multi_language_needed", False)
        )
        imagery_style_guide = self._define_imagery_style_guide(
            brand_playbook_data,
            target_audience_persona_data,
            module2_trend_research_output
        )
        video_style_guide = self._define_video_style_guide(
            brand_playbook_data,
            target_audience_persona_data,
            module2_trend_research_output
        )
        layout_principles = self._define_layout_principles(
            color_system,
            typography_system,
            visual_design_principles_kb
        )
        
        # 组装完整VI系统
        vi_system = {
            "color_palette_system": color_system,
            "typography_system": typography_system,
            "imagery_style_guide": imagery_style_guide,
            "video_style_guide": video_style_guide,
            "layout_and_composition": layout_principles,
            "trend_adaptation": module2_trend_research_output.get("trend_recommendation", {}),
            "version": "1.0.0",
            "creation_date": "2025-06-20",
            "designer_notes": "本VI系统专为社交媒体场景优化，确保品牌视觉一致性与传播效果"
        }
        print("模块3: 社交媒体视觉识别系统构建完成")
        return vi_system


# ------------------------- 测试函数 -------------------------
def test_define_color_palette():
    """测试色彩体系生成功能"""
    social_vi = SocialVISystem()
    existing_colors = "['#0A7AFF', '#FFD60A']"
    brand_tone = "['科技感', '信赖', '活力']"
    audience_pref = "['明亮', '现代', '高对比']"
    industry_trends = [
        {"trend_name": "莫兰迪色系", "colors": ['#E0E0E0', '#BDBDBD']},
        {"trend_name": "高饱和蓝", "colors": ['#0A7AFF']}
    ]
    visual_design_kb = {"color_psychology": {"blue": "科技、信任", "yellow": "活力、乐观"}}
    result = social_vi._define_color_palette(
        existing_colors, brand_tone, audience_pref, industry_trends, visual_design_kb
    )
    print(result)

def test_define_typography_system():
    """测试字体系统生成功能"""
    social_vi = SocialVISystem()
    existing_fonts = "['思源黑体 CN Regular', 'Arial']"
    brand_playbook = {
        'brand_persona_keywords_list_str': "['科技感', '现代', '国际化']",
        'brand_tone_descriptors_list_str': "['专业', '简洁']",
        'multi_language_needed': True
    }
    result = social_vi._define_typography_system(
        existing_fonts, brand_playbook, multi_language_needed=True
    )
    print(result)

def test_define_imagery_style_guide():
    """测试图像风格指南生成功能"""
    social_vi = SocialVISystem()
    brand_playbook = {
        'brand_tone_descriptors_list_str': "['真实', '亲切', '现代']"
    }
    audience_persona = {
        'visual_preferences_keywords_list_str': "['生活化场景', '明亮色调', '高质感']"
    }
    trend_research = {
        "current_industry_trends": [
            {"trend_name": "生活化摄影", "description": "真实场景、自然光"},
            {"trend_name": "扁平插画", "description": "简洁明快"}
        ]
    }
    result = social_vi._define_imagery_style_guide(
        brand_playbook, audience_persona, trend_research
    )
    print(result)

# 取消注释以下行以运行测试
test_define_color_palette()
test_define_typography_system()
test_define_imagery_style_guide()