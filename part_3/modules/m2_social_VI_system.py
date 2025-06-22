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
  
class VISystemDesigner(ABC):  
    """视觉识别系统设计师基类"""  
      
    def __init__(self, name: str, expertise: str, model_type: ModelType = ModelType.GPT_4O):  
        self.name = name  
        self.expertise = expertise  
        self.model = ModelFactory.create(  
            model_platform=ModelPlatformType.OPENAI,  
            model_type=model_type,  
        )  
        self.agent = self._create_agent()  
      
    @abstractmethod  
    def _create_system_message(self) -> str:  
        """创建系统消息"""  
        pass  
      
    def _create_agent(self) -> ChatAgent:  
        """创建ChatAgent"""  
        sys_msg = BaseMessage.make_assistant_message(  
            role_name=self.name,  
            content=self._create_system_message(),  
        )  
        return ChatAgent(system_message=sys_msg, model=self.model)  
  
class BrandIdentityDesigner(VISystemDesigner):  
    """品牌识别设计师"""  
      
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
          
        请提供专业的设计建议和评估，评分标准1-5分。  
        """)  
  
class DigitalMediaDesigner(VISystemDesigner):  
    """数字媒体设计师"""  
      
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
        4. 视觉层次和信息传达效率  
          
        请从数字媒体角度提供专业评估，评分1-5分。  
        """)  
  
class PrintMediaDesigner(VISystemDesigner):  
    """印刷媒体设计师"""  
      
    def __init__(self):  
        super().__init__(  
            name="印刷媒体设计师",  
            expertise="印刷品设计、包装设计、物料设计"  
        )  
      
    def _create_system_message(self) -> str:  
        return textwrap.dedent("""  
        你是经验丰富的印刷媒体设计师，专长：  
        - 包装设计与结构优化  
        - 印刷工艺与材质选择  
        - 宣传物料设计  
        - 色彩管理与印刷适配  
          
        设计考量：  
        1. 印刷工艺的可行性和成本控制  
        2. 材质选择与环保要求  
        3. 货架陈列效果  
        4. 品牌一致性在物理媒介的体现  
          
        请提供印刷媒体专业建议，评分1-5分。  
        """)  
  
class UserExperienceDesigner(VISystemDesigner):  
    """用户体验设计师"""  
      
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
          
        请从用户体验角度进行专业评估，评分1-5分。  
        """)  
  
class MarketResearcher(VISystemDesigner):  
    """市场研究员"""  
      
    def __init__(self):  
        super().__init__(  
            name="市场研究员",  
            expertise="市场趋势分析、竞品研究、消费者洞察"  
        )  
        # 添加搜索工具  
        search_toolkit = SearchToolkit()  
        self.search_tools = [  
            FunctionTool(search_toolkit.search_google),  
            FunctionTool(search_toolkit.search_duckduckgo),  
        ]  
        self.agent.tools = self.search_tools  
      
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


class VISystemDesignTeam:  
    """VI系统设计团队"""  
      
    def __init__(self, team_name: str = "VI系统设计团队"):  
        self.team_name = team_name  
        self.workforce = Workforce(team_name)  
        self.designers = self._initialize_team()  
        self._setup_workforce()  
      
    def _initialize_team(self) -> Dict[str, VISystemDesigner]:  
        """初始化设计团队成员"""  
        return {  
            "brand_identity": BrandIdentityDesigner(),  
            "digital_media": DigitalMediaDesigner(),   
            "print_media": PrintMediaDesigner(),  
            "user_experience": UserExperienceDesigner(),  
            "market_researcher": MarketResearcher(),  
        }  
      
    def _setup_workforce(self):  
        """设置workforce""" 
          
        self.workforce.add_single_agent_worker(  
            "市场研究员 - 负责收集行业趋势、竞品分析和消费者洞察",  
            worker=self.designers["market_researcher"].agent,  
        ).add_single_agent_worker(  
            "品牌识别设计师 - 负责品牌标识、色彩和字体系统设计",  
            worker=self.designers["brand_identity"].agent,  
        ).add_single_agent_worker(  
            "数字媒体设计师 - 负责数字平台视觉设计和用户界面优化",  
            worker=self.designers["digital_media"].agent,  
        ).add_single_agent_worker(  
            "印刷媒体设计师 - 负责包装设计和印刷物料设计",  
            worker=self.designers["print_media"].agent,  
        ).add_single_agent_worker(  
            "用户体验设计师 - 负责用户研究和可用性评估",  
            worker=self.designers["user_experience"].agent,  
        )  
    
    def create_design_task(self,   
                          project_name: str,  
                          brand_info: str,  
                          design_requirements: str,  
                          target_audience: str) -> Task:  
        """创建设计任务""" 
          
        task_content = f"""  
        请为{project_name}进行全面的VI系统设计评估和优化建议：  
          
        1. 市场研究员：分析当前行业视觉趋势和竞品策略  
        2. 品牌识别设计师：评估品牌标识、色彩和字体系统  
        3. 数字媒体设计师：分析数字平台适配性和用户界面设计  
        4. 印刷媒体设计师：评估包装和印刷物料设计  
        5. 用户体验设计师：从用户角度评估整体视觉体验  
        6. 整合所有专家意见，提供综合性的VI系统优化方案  
          
        设计要求：{design_requirements}  
        """  
          
        additional_info = f"""  
        品牌信息：{brand_info}  
        目标受众：{target_audience}  
        项目名称：{project_name}  
        """  
          
        return Task(  
            content=task_content,  
            additional_info=additional_info,  
            id=f"vi_design_{project_name.lower().replace(' ', '_')}",  
        )  
      
    def execute_design_project(self, task: Task) -> str:  
        """执行设计项目""" 
          
        print(f"开始执行{self.team_name}设计项目...")  
        completed_task = self.workforce.process_task(task)  
        return completed_task.result  
      
    def get_team_info(self) -> Dict[str, str]:  
        """获取团队信息"""  
        return {  
            "team_name": self.team_name,  
            "members": [designer.name for designer in self.designers.values()],  
            "capabilities": [designer.expertise for designer in self.designers.values()],  
        }  
  
  
def m2(brand_info: str, target_audience: str):
    """主函数示例"""  
    # 创建VI系统设计团队  
    vi_team = VISystemDesignTeam("EcoGarden VI设计团队")  
      
    # 创建设计任务  
    design_task = vi_team.create_design_task(  
        project_name="VISystem",  
        brand_info=brand_info,  
        design_requirements="""  
        1. 设计现代简约的品牌标识  
        2. 建立完整的色彩和字体系统  
        3. 确保跨平台一致性  
        4. 体现产品的风格和设计理念  
        5. 适配小红书、抖音等社交媒体平台  
        """,  
        target_audience=target_audience 
    )
    