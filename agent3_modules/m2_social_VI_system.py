import textwrap
import json
import os
import sys
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Dict, Any, List

from dotenv import load_dotenv
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.toolkits import SearchToolkit, FunctionTool



# 使用绝对导入
from utils import clean_json_string, output

# --- Agent 蓝图定义 (作为辅助类，保留在顶层) ---
class VISystemDesigner(ABC):
    def __init__(self, name: str, expertise: str, model: Any):
        self.name = name
        self.expertise = expertise
        self.model = model
        self.agent = self._create_agent()
    @abstractmethod
    def _create_system_message(self) -> str: pass
    def _create_agent(self) -> ChatAgent:
        sys_msg = BaseMessage.make_assistant_message(role_name=self.name, content=self._create_system_message())
        return ChatAgent(system_message=sys_msg, model=self.model)

class BrandIdentityDesigner(VISystemDesigner):
    def __init__(self, model: Any): super().__init__("品牌识别设计师", "品牌标识、色彩系统", model)
    def _create_system_message(self) -> str: return textwrap.dedent("你是一位资深的品牌识别设计师...")

class UserExperienceDesigner(VISystemDesigner):
    def __init__(self, model: Any): super().__init__("用户体验设计师", "用户研究、可用性测试", model)
    def _create_system_message(self) -> str: return textwrap.dedent("你是专业的用户体验设计师...")

class VIOutputSynthesizer(VISystemDesigner):
    def __init__(self, model: Any):
        super().__init__("VI系统输出整合师", "将摘要转化为结构化的JSON", model)
    def _create_system_message(self) -> str:
        return textwrap.dedent("""
        你是一位专业的VI系统整合师。你的任务是接收一份关于VI设计的**摘要报告**。
        你必须将这份摘要中的核心信息，转化成一个完整、详细、结构化的VI系统规范。
        最终的输出必须是一个严格的JSON格式对象，不得包含任何JSON格式之外的解释性文字或前言。
        """)

# --- 核心流程函数 (作为辅助函数，保留在顶层) ---

def get_expert_statements(
    agents: Dict[str, VISystemDesigner], brand_info: str, design_requirements: str, target_audience: str, _trend
) -> str:
    """第一步：让每位专家仅发言一次，收集所有独立观点。"""
    output("GREY", "[步骤1] 正在收集各位专家的独立陈述...")
    statements: List[str] = []
    initial_prompt = f"""
    项目启动：为进行VI系统设计。
    品牌内容：{brand_info}
    核心设计要求：{design_requirements}
    目标受众：{target_audience}
    市场趋势分析:{_trend}
    请根据以上信息和你的专业领域，直接陈述你的核心设计建议、分析或考量。
    """
    for agent_name, agent_instance in agents.items():
        response = agent_instance.agent.step(BaseMessage.make_user_message(role_name="Project Lead", content=initial_prompt))
        if response.msgs and response.msgs[0].content:
            output("GREY", f"{response.msgs[0].content}")
            statements.append(f"--- 来自 {agent_instance.name} 的观点 ---\n{response.msgs[0].content}")
    return "\n\n".join(statements)

def summarize_statements(statements: str, model: Any) -> str:
    """第二步：对所有观点进行摘要。"""
    output("GREY", "[步骤2] 正在生成讨论摘要...")
    summarizer_sys_msg = BaseMessage.make_assistant_message(role_name="会议记录员", content="你是一位专业的会议记录员。请阅读以下陈述，并整合成一份连贯、精炼的摘要报告。")
    summarizer_agent = ChatAgent(system_message=summarizer_sys_msg, model=model)
    prompt = f"请根据以下专家陈述，生成一份摘要报告：\n\n{statements}"
    response = summarizer_agent.step(BaseMessage.make_user_message(role_name="Human", content=prompt))
    output("GREY", f"摘要报告:\n{response.msgs[0].content}\n")
    return response.msgs[0].content if response.msgs and response.msgs[0].content else "摘要生成失败。"

def create_final_json(synthesizer: VISystemDesigner, summary: str) -> str:
    """第三步：整合师根据摘要报告，生成最终的JSON。"""
    output("GREY", "[步骤3] 正在根据摘要生成最终JSON...")
    prompt = f"这是设计会议的摘要报告。请根据这份摘要，严格按照你的系统指令，生成最终的VI系统规范JSON文件。\n\n--- 摘要报告 ---\n{summary}"
    response = synthesizer.agent.step(BaseMessage.make_user_message(role_name="Human", content=prompt))
    return response.msgs[0].content if response.msgs and response.msgs[0].content else '{"error": "JSON生成失败。"}'


# --- 主功能函数 ---
load_dotenv()
SF_API_KEY = os.getenv("FLOW_API")

if not SF_API_KEY:
    output("RED", "请在 .env 文件中设置您的 GEMINI_API_KEY。")
    exit(1)

def m2(brand_info: str, target_audience: str, _trend_analyze) -> dict:
    """
    接收品牌信息，执行三步式VI设计流程，并返回最终的JSON结果。

    Args:
        brand_info (str): 品牌信息,市场趋势分析
        target_audience (str): 目标受众。
        trend_analyze (str): 。

    Returns:
        dict: 包含VI设计规范的Python字典。
    """
    # 临时的日志记录器

    # 1. 初始化环境和模型

    output("GREY", "正在初始化 Gemini 模型...")
    dpsk_model = ModelFactory.create(
        model_platform=ModelPlatformType.SILICONFLOW,
        model_type='Pro/deepseek-ai/DeepSeek-V3',
        model_config_dict={
            "max_tokens": 8192,
            "temperature": 0.01
        },
        api_key=SF_API_KEY,
    )
    output("GREY", "m2 模型初始化完成。")

    # 2. 定义固定的设计要求
    design_requirements = "设计一个现代、简约且具有科技感的品牌标识，并建立完整的色彩和构图系统。"

    # 3. 创建常驻的 Agent 实例
    experts = {
        "brand_dentity": BrandIdentityDesigner(model=dpsk_model),
        "user_experience": UserExperienceDesigner(model=dpsk_model),
    }
    synthesizer = VIOutputSynthesizer(model=dpsk_model)

    statements = get_expert_statements(
        experts, brand_info, design_requirements, target_audience, _trend_analyze
    )
    summary = summarize_statements(statements, dpsk_model)
    final_answer_str = create_final_json(synthesizer, summary)

    # 5. 清理并返回字典
    try:
        cleaned_str = clean_json_string(final_answer_str)
        if not cleaned_str:
            raise json.JSONDecodeError("清理后的字符串为空。", "", 0)
        
        final_json_obj = json.loads(cleaned_str)
        return final_json_obj
    except json.JSONDecodeError as e:
        output("RED", f"最终输出不是有效的JSON。错误: {e}")
        output("RED", f"原始输出: {final_answer_str}")
        return {"error": "未能解析最终结果为JSON。", "raw_output": final_answer_str}

