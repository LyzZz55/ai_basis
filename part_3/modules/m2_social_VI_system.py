from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.societies.workforce import Workforce
from camel.tasks import Task
from camel.toolkits import SearchToolkit
from camel.toolkits import FunctionTool
import textwrap
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")

gemini_model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_1_5_FLASH,
    model_config_dict={
        "max_tokens": 8192,
        "temperature": 0.7
    },
    api_key=GEMINI_API_KEY
)
dpskv3_model = ModelFactory.create(
    model_platform=ModelPlatformType.SILICONFLOW,
    model_type='Pro/deepseek-ai/DeepSeek-R1',
    model_config_dict={
        "max_tokens": 8192,
        "temperature": 0.7
    },
    api_key=SF_API_KEY,
)

class VISystemDesigner(ABC):
    """Abstract base class for Visual Identity System Designers."""

    def __init__(self, name: str, expertise: str):
        self.name = name
        self.expertise = expertise
        self.agent = self._create_agent()

    @abstractmethod
    def _create_system_message(self) -> str:
        """Creates the system message for the agent."""
        pass

    def _create_agent(self) -> ChatAgent:
        """Creates the ChatAgent."""
        sys_msg = BaseMessage.make_assistant_message(
            role_name=self.name,
            content=self._create_system_message(),
        )
        return ChatAgent(system_message=sys_msg, model=gemini_model)

class BrandIdentityDesigner(VISystemDesigner):
    """Brand Identity Designer"""

    def __init__(self):
        super().__init__(
            name="品牌识别设计师",
            expertise="品牌标识、色彩系统、字体系统设计"
        )

    def _create_system_message(self) -> str:
        return textwrap.dedent("""
        你是一位资深的品牌识别设计师，专精于：
        - 品牌标识(Logo)设计与优化
        - 品牌色彩系统规划
        - 字体系统选择与搭配
        - 品牌视觉元素统一性

        设计原则：
        1. 确保品牌识别的独特性和辨识度
        2. 考虑不同媒介的适用性
        3. 保持视觉系统的一致性
        4. 符合目标受众的审美偏好

        请提供专业的设计建议和评估。
        """)

class DigitalMediaDesigner(VISystemDesigner):
    """Digital Media Designer"""

    def __init__(self):
        super().__init__(
            name="数字媒体设计师",
            expertise="数字平台视觉设计、用户界面设计"
        )

    def _create_system_message(self) -> str:
        return textwrap.dedent("""
        你是专业的数字媒体设计师，擅长：
        - 社交媒体平台视觉设计
        - 移动端界面设计适配
        - 数字广告创意设计
        - 用户体验优化

        关注重点：
        1. 不同平台的设计规范适配
        2. 移动优先的设计理念
        3. 用户交互体验优化
        4. 视觉层次和美感

        请从数字媒体角度提供专业评估。
        """)

class UserExperienceDesigner(VISystemDesigner):
    """User Experience Designer"""

    def __init__(self):
        super().__init__(
            name="用户体验设计师",
            expertise="用户研究、交互设计、可用性测试"
        )

    def _create_system_message(self) -> str:
        return textwrap.dedent("""
        你是专业的用户体验设计师，专注：
        - 用户行为分析与洞察
        - 视觉设计的可用性评估
        - 用户旅程优化
        - A/B测试设计与分析

        评估维度：
        1. 视觉设计对用户认知的影响
        2. 品牌识别的易理解性
        3. 跨平台用户体验一致性
        4. 可访问性和包容性设计

        请从用户体验角度进行专业评估。
        """)

class MarketResearcher(VISystemDesigner):
    """Market Researcher"""

    def __init__(self):
        super().__init__(
            name="市场研究员",
            expertise="市场趋势分析、竞品研究、消费者洞察"
        )
        search_toolkit = SearchToolkit()
        self.agent.tools = [
            FunctionTool(search_toolkit.search_google),
        ]

    def _create_system_message(self) -> str:
        return textwrap.dedent("""
        你是专业的市场研究员，负责：
        - 行业视觉趋势分析
        - 竞品视觉策略研究
        - 目标受众偏好调研
        - 市场机会识别

        研究方法：
        1. 使用搜索工具收集最新市场信息
        2. 分析竞品视觉策略优劣
        3. 识别市场空白和机会点
        4. 提供数据支撑的建议

        请提供基于市场数据的专业分析。
        """)

class VIOutputSynthesizer(VISystemDesigner):
    """VI System Output Synthesizer and Formatter."""

    def __init__(self):
        super().__init__(
            name="VI系统输出整合师",
            expertise="整合设计团队的分析，并以结构化的JSON格式输出最终的VI系统规范"
        )

    def _create_system_message(self) -> str:
        return textwrap.dedent("""
        你是一位专业的VI系统整合师和技术文档专家。
        你的唯一任务是接收来自市场研究员、品牌识别设计师、数字媒体设计师和用户体验设计师的分析和建议。
        然后，你必须将这些零散的信息整合成一个完整、详细、结构化的VI系统规范。
        最终的输出必须是一个严格的JSON格式对象，不得包含任何JSON格式之外的解释性文字或前言。

        你的输出JSON必须遵循以下结构：
        {
          "visualAssetsAnalysis": {
            "summary": "对现有视觉资产的评估和延展性分析的总结。",
            "strengths": ["优点1", "优点2"],
            "weaknesses": ["缺点1", "缺点2"],
            "opportunities": ["机会1", "机会2"]
          },
          "viSystemProposal": {
            "colorPalette": {
              "primary": {"name": "品牌主色", "hex": "#RRGGBB"},
              "secondary": [{"name": "辅助色1", "hex": "#RRGGBB"}],
              "accent": [{"name": "强调色1", "hex": "#RRGGBB"}],
              "background": [{"name": "背景色1", "hex": "#RRGGBB"}],
              "accessibilityNotes": "关于色彩组合在不同背景下的可读性和无障碍设计的说明。"
            },
            "typographySystem": {
              "primaryFont": {"fontFamily": "字体名称", "purpose": "主标题", "weights": ["Regular", "Bold"], "notes": "版权、多语言支持、跨平台显示效果等说明。"},
              "secondaryFont": {"fontFamily": "字体名称", "purpose": "正文", "weights": ["Regular"], "notes": "版权、多语言支持、跨平台显示效果等说明。"},
              "usageGuidelines": {
                "h1": {"fontSize": "32px", "fontWeight": "Bold", "lineHeight": "1.2"},
                "body": {"fontSize": "16px", "fontWeight": "Regular", "lineHeight": "1.5"}
              }
            },
            "imageryStyleGuide": {
              "photography": {
                "theme": ["人物", "产品", "场景"],
                "composition": ["黄金分割", "对称", "引导线"],
                "lighting": "自然光优先，辅以柔和的影棚光。",
                "colorTone": "整体偏暖色调，低饱和度，营造亲和感。",
                "depthOfField": "多使用浅景深突出主体。",
                "mood": "积极、真实、有活力。",
                "postProcessing": "风格统一的滤镜，避免过度修饰。"
              },
              "illustrationAndGraphics": {
                "style": "扁平风 (Flat Design)",
                "lineWeight": "统一使用2px的线条粗细。",
                "symbolSystem": "建立一套简洁、表意明确的图形符号系统。",
                "dataVisualization": "图表设计规范，确保数据清晰传达，配色遵循品牌色彩体系。"
              }
            },
            "videoStyleGuide": {
              "pacing": "根据内容决定，产品介绍视频节奏快，品牌故事视频节奏舒缓。",
              "transitions": "推荐使用简洁的淡入淡出或切割转场。",
              "subtitleStyle": {"font": "与正文字体一致", "size": "24px", "color": "白色带半透明黑色描边"},
              "musicStyle": ["轻快的电子音乐", "氛围感的纯音乐"],
              "colorGrading": "建议使用统一的LUTs，以匹配摄影的色调。",
              "animatedLogo": "在视频开头或结尾使用指定的动态Logo演绎效果。"
            },
            "layoutAndComposition": {
              "gridSystem": "推荐使用8点栅格系统，保证跨平台一致性。",
              "whiteSpace": "强调留白的使用，创造简洁、高级的视觉感受。",
              "visualHierarchy": "通过大小、颜色、位置关系建立清晰的信息层级。",
              "logoUsage": "定义Logo在不同版式中的最小尺寸、安全边距和禁用场景。"
            }
          }
        }
        请严格按照此JSON结构和字段要求进行填充和输出。
        """)


class VISystemDesignTeam:
    """VI System Design Team"""

    def __init__(self, team_name: str = "VI系统设计团队"):
        self.team_name = team_name
        self.workforce = Workforce(
            description=team_name,
            new_worker_agent_kwargs={'model': gemini_model},
            coordinator_agent_kwargs={'model': dpskv3_model},
            task_agent_kwargs={'model': gemini_model}
        )
        self.designers = self._initialize_team()
        self._setup_workforce()

    def _initialize_team(self) -> Dict[str, VISystemDesigner]:
        """Initializes the design team members."""
        return {
            "brand_identity": BrandIdentityDesigner(),
            "digital_media": DigitalMediaDesigner(),
            "user_experience": UserExperienceDesigner(),
            "market_researcher": MarketResearcher(),
            "output_synthesizer": VIOutputSynthesizer(),
        }

    def _setup_workforce(self):
        """Sets up the workforce."""
        self.workforce.add_single_agent_worker(
            "市场研究员 - 负责收集行业趋势、竞品分析和消费者洞察",
            worker=self.designers["market_researcher"].agent,
        ).add_single_agent_worker(
            "品牌识别设计师 - 负责最具体的品牌标识、色彩和字体系统设计",
            worker=self.designers["brand_identity"].agent,
        ).add_single_agent_worker(
            "数字媒体设计师 - 负责研究设计VI系统能否符合数字平台视觉设计和用户界面",
            worker=self.designers["digital_media"].agent,
        ).add_single_agent_worker(
            "用户体验设计师 - 负责评判VI设计能否满足对应的目标受众的喜好",
            worker=self.designers["user_experience"].agent,
        ).add_single_agent_worker(
            "VI系统输出整合师 - 负责将所有分析和设计整合成最终的JSON格式VI规范文档",
            worker=self.designers["output_synthesizer"].agent,
        )

    def create_design_task(
        self,
        brand_info: str,
        design_requirements: str,
        target_audience: str
    ) -> Task:
        """Creates the design task with detailed instructions."""
        task_content = f"""
        请各位专家协作，为品牌进行一次全面的VI系统设计。请严格按照以下步骤执行：

        第一步：进行背景分析与评估。
        - 市场研究员：分析当前行业视觉趋势、竞品视觉策略，并结合目标受众的偏好，提供数据支撑的洞察。
        - 品牌识别设计师、数字媒体设计师、用户体验设计师：基于市场研究员的分析，结合品牌信息，共同评估品牌现有视觉资产（如果有），并分析其延展性、优势与劣势。

        第二步：进行创意设计与规范制定。
        - 基于第一步的分析，各位设计师共同协作，提出一个全新的、或优化后的综合性VI系统方案。
        - 你们的讨论和设计需要覆盖以下所有方面，并提供具体、可执行的细节：
          - **色彩体系 (Color Palette):** 定义品牌主色、辅助色、强调色、背景色。要考虑易读性和情感表达，并为无障碍设计提出建议。提供 HEX值。
          - **字体系统 (Typography System):** 推荐 1-2 款主标题字体、1 款正文字体（考虑版权、多语言支持、跨平台显示效果）。定义不同场景下的字号、字重、行距规范。
          - **图像风格指南 (Imagery Style Guide):** 详细定义摄影风格（主题、构图、光线、色调、景深、人物情绪、后期风格）和插画/图形元素风格（风格、线条粗细、图形符号系统、数据可视化图表规范）。
          - **视频风格指南 (Video Style Guide):** 定义视频的节奏、转场、字幕样式、配乐风格和画面调色建议（如LUTs建议）、动态 Logo 演绎。
          - **版式与构图原则 (Layout & Composition Principles):** 建立栅格系统应用、留白、视觉焦点引导、信息层级排布、品牌元素（如 Logo）在不同版式中的规范应用。

        第三步：最终输出。
        - **VI系统输出整合师**: 你的任务是最后一步。请收集并整合以上所有专家的分析、讨论和设计方案。
        - 你必须将所有内容严格按照你系统提示词中定义的JSON结构进行格式化输出。最终结果必须是一个完整的、有效的JSON对象，包含`visualAssetsAnalysis`和`viSystemProposal`两个顶级键。在最终输出中，除了JSON本身，不要添加任何其他文字、注释或解释。

        设计要求：{design_requirements}
        """

        additional_info = f"""
        品牌信息：{brand_info}
        目标受众：{target_audience}
        已有视觉信息：{current_vi_info}
        """

        return Task(
            content=task_content,
            additional_info=additional_info,
            id=f"vi_design",
        )

    def execute_design_project(self, task: Task) -> str:
        """Executes the design project."""
        print(f"开始执行VI设计项目...")
        completed_task = self.workforce.process_task(task)
        return completed_task.result

    def get_team_info(self) -> Dict[str, str]:
        """Gets team information."""
        return {
            "team_name": self.team_name,
            "members": [designer.name for designer in self.designers.values()],
            "capabilities": [designer.expertise for designer in self.designers.values()],
        }


def m2( brand_info: str, target_audience: str):
    """Main function example"""
    # Create VI system design team
    vi_team = VISystemDesignTeam(f"VI设计团队")

    # Create design task
    design_task = vi_team.create_design_task(
        brand_info=brand_info,
        design_requirements="""
        1. 设计一个现代、简约且具有科技感的品牌标识。
        2. 建立完整的色彩和字体系统。
        3. 体现品牌的创新、专业和用户友好的核心价值观。
        4. 视觉系统需要高度适配小红书、抖音、Bilibili等主流社交媒体平台。
        """,
        target_audience=target_audience
    )
    # Process a task
    result = vi_team.execute_design_project(design_task)
    print("---### Final VI System Design (JSON)---")
    print(result)
