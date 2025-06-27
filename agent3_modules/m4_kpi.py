########################################################################################
# 基于内容日历，制定#标签策略，设计互动与UGC激励方案
# 基于Agent 1的初步KPI框架和Agent 2的内容规划，细化各平台、各内容类型的核心KPI，并建议数据分析维度和报告模板
########################################################################################

import sys
from pathlib import Path
# 获取项目根目录并添加到sys.path
project_root = str(Path(__file__).parent.parent.parent)  # 根据实际结构调整
sys.path.append(project_root)
# 使用绝对导入
from utils import output

import textwrap

from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.tasks import Task
from camel.toolkits import FunctionTool, SearchToolkit
from camel.types import ModelPlatformType, ModelType
from camel.societies.workforce import workforce

from dotenv import load_dotenv
import os
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")

from camel.agents import ChatAgent  
from camel.models import ModelFactory  
from camel.types import ModelPlatformType, ModelType  
from camel.toolkits import SearchToolkit, FunctionTool  
from camel.messages import BaseMessage  
  
class KPIAnalysisAgent:  
    def __init__(self, model_config):  
        # 创建系统消息，定义Agent角色  
        system_message = BaseMessage.make_assistant_message(  
            role_name="KPI分析专家",  
            content="""
            你是一位资深的数字营销KPI分析专家，专门负责：  
            1. 分析和扩展简单的KPI框架  
            2. 基于行业标准和最佳实践提供详细的KPI细化建议  
            3. 运用搜索工具获取最新的行业基准数据和相关KPI设计案例经验
            4. 为每个KPI提供具体的测量方法、计算公式和优化建议  
            5. 识别KPI之间的关联性和影响因素
              
            提供必要的分析解释"""  
        )  
          
        # 配置搜索工具  
        search_toolkit = SearchToolkit()  
        tools = [  
            FunctionTool(search_toolkit.search_duckduckgo),  
            FunctionTool(search_toolkit.search_baidu),  
            FunctionTool(self.calculate_kpi_benchmarks),  
        ]  
          
        # 创建ChatAgent  
        self.agent = ChatAgent(  
            system_message=system_message,  
            model=model_config,  
            tools=tools  
        )  
      
    def calculate_kpi_benchmarks(self, industry: str, platform: str, kpi_type: str) -> str:  
        """计算行业KPI基准值  
        Args:  
            industry (str): 行业类型，如美妆、电商、科技等  
            platform (str): 平台名称，如抖音、小红书、微信等    
            kpi_type (str): KPI类型，如完播率、转化率、互动率等  
        Returns:  
            str: 包含基准数据的详细分析结果  
    """
        # TODO 集成真实的基准数据库或API  
        benchmarks = {  
            "抖音": {  
                "视频完播率": "行业平均: 45-60%, 优秀: 65%+",  
                "互动率": "行业平均: 3-5%, 优秀: 8%+",  
                "转化率": "行业平均: 1-3%, 优秀: 5%+"  
            },  
            "小红书": {  
                "UGC投稿量": "活跃品牌: 500-1000篇/周",  
                "笔记互动率": "行业平均: 2-4%, 优秀: 6%+",  
                "种草转化率": "行业平均: 0.5-2%, 优秀: 3%+"  
            }  
        }  
          
        result = benchmarks.get(platform, {}).get(kpi_type, "暂无基准数据")  
        return f"{platform}平台{kpi_type}基准: {result}"  
      
    def expand_kpi_framework(self, brand_info_simple_kpi_table: str, content_calendar: str) -> str:  
        """扩展KPI框架的主要方法"""  
        prompt = f"""  
  
  
        请执行以下任务：  
      - 基于初步KPI框架和内容规划，细化每个平台、每种内容类型的核心、次核心、诊断性 KPIs。
      - **示例：**
        - **认知层：** 曝光量、覆盖人数、品牌搜索量增长。
        - **互动层：** 点赞、评论、分享、收藏、转发率、互动率、UGC 产出数量。
        - **引导层：** 点击率 (CTR)、落地页访问量、表单提交数、App 下载量。
        - **转化层 (若可追踪)：** 销售额、订单量、ROI。
        - **品牌健康度：** 粉丝增长数、净推荐值 (NPS)、品牌声量情感正负比。
      - 建议数据分析的维度（如按内容主题、按 Persona、按发布时段）和报告频率（如周报/月报）。
  
        输出格式要求：  
        - 详细的KPI扩展表格  
        - 每个KPI的具体分析  
        
        
        根据
        提供的品牌信息、简单的KPI框架：
        {brand_info_simple_kpi_table}
        
        内容规划：
        {content_calendar}
        """  
          
        response = self.agent.step(prompt)  
        return response.msgs[0].content  
  
# 使用示例  
def create_kpi_analysis_agent():  
    model = ModelFactory.create(  
        model_platform=ModelPlatformType.SILICONFLOW,
        model_type='Pro/deepseek-ai/DeepSeek-V3',
        model_config_dict={
            "max_tokens": 4096,
            "temperature": 0.01
        },
        api_key=SF_API_KEY,
    )  
      
    return KPIAnalysisAgent(model)


def kpi_working(brand_and_simple_kpi: str, content_calendar: str):
    kpi_agent = create_kpi_analysis_agent()
    
    # 执行KPI扩展分析  
    expanded_analysis = kpi_agent.expand_kpi_framework(brand_and_simple_kpi, content_calendar)  
    
    return expanded_analysis



'''
以下是基于您的KPI框架的深度扩展和细化分析：

---

### **1. KPI扩展表格**
| 营销目标          | 平台       | KPI类型               | 目标值 | 基准数据                 | 补充KPI                     |
|------------------|------------|----------------------|-------|--------------------------|----------------------------|
| 月光面膜认知度40% | 抖音       | 视频完播率           | ≥65%  | 行业优秀: 65%+           | 互动率（点赞+评论+转发）     |
| 新增会员5,000人   | 全域       | 会员转化率           | 7.2%  | 暂无基准数据             | 新客获取成本（CAC）          |
| UGC 10,000+      | 小红书     | UGC投稿量/周         | 800篇 | 活跃品牌: 500-1000篇/周 | UGC互动率（点赞+收藏+评论）  |
| 会员复购率35%     | 私域       | 90天复购频次         | ≥2.1次| 暂无基准数据             | 客户生命周期价值（LTV）      |

---

### **2. 详细KPI分析**

#### **2.1 视频完播率（抖音）**
- **定义**: 用户完整观看视频的百分比。
- **公式**: (完整观看视频的用户数 / 视频总观看用户数) × 100%
- **测量方法**: 通过抖音后台数据分析工具获取。
- **关联性**: 高完播率通常伴随高互动率，可能提升品牌认知度。
- **优化建议**:
  - 前5秒抓住用户注意力（悬念、痛点或福利）。
  - 视频时长控制在15-30秒。
  - 测试不同内容形式（教程、测评、故事等）。

#### **2.2 会员转化率（全域）**
- **定义**: 访问用户转化为会员的百分比。
- **公式**: (新增会员数 / 总访问用户数) × 100%
- **测量方法**: 通过CRM系统或数据分析工具追踪。
- **关联性**: 转化率高可能降低CAC，但需结合复购率评估长期价值。
- **优化建议**:
  - 注册流程简化（一键注册、第三方登录）。
  - 提供新会员礼包（如折扣券、试用装）。

#### **2.3 UGC投稿量（小红书）**
- **定义**: 每周用户生成内容的数量。
- **公式**: 直接统计每周UGC投稿数。
- **测量方法**: 通过小红书品牌号后台或第三方工具监控。
- **关联性**: UGC投稿量与品牌口碑直接相关，需关注互动率。
- **优化建议**:
  - 发起UGC活动（如“晒单有奖”）。
  - KOL合作带动普通用户参与。

#### **2.4 90天复购频次（私域）**
- **定义**: 会员在90天内重复购买的次数。
- **公式**: (复购会员数 / 总会员数) × 100%
- **测量方法**: 通过CRM系统追踪会员购买记录。
- **关联性**: 高复购频次可能提升LTV，但需结合客单价分析。
- **优化建议**:
  - 定期推送个性化推荐（如生日礼包）。
  - 会员积分体系激励复购。

---

### **3. 补充重要KPI**
- **互动率（抖音）**: 衡量用户对内容的参与度，公式为（点赞+评论+转发）/ 观看数 × 100%。
- **新客获取成本（CAC）**: 公式为总营销费用 / 新增会员数。
- **UGC互动率（小红书）**: 公式为（点赞+收藏+评论）/ UGC投稿量 × 100%。
- **客户生命周期价值（LTV）**: 公式为平均客单价 × 年均购买频次 × 平均留存年限。

---

### **4. 监控预警机制设计**
- **频率**: 每日监控关键KPI（如UGC投稿量、互动率），每周汇总分析。
- **预警阈值**:
  - 视频完播率低于50%时，需优化内容策略。
  - UGC投稿量连续两周低于500篇，启动激励活动。
- **工具**: 使用Google Analytics、抖音/小红书后台、CRM系统等。

---

### **5. 行动计划**
| KPI               | 优化策略                          | 责任团队       | 时间节点   |
|-------------------|----------------------------------|---------------|------------|
| 视频完播率        | 测试3种视频开头形式               | 内容团队       | 2周        |
| 会员转化率        | 上线新会员礼包                    | 运营团队       | 1个月      |
| UGC投稿量         | 合作5名KOL带动投稿                | 市场团队       | 3周        |
| 90天复购频次      | 推出会员积分换购活动              | 会员运营团队   | 1个月      |
'''