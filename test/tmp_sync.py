# dictExam = {
#     "test1": "a",
#     "test2": ["x", "y"],
# }

# print(f'aaaaa{dictExam}')

from camel.agents import ChatAgent
from camel.models import OpenAIChatModel  # 示例：假设使用OpenAI模型

# 配置正确的API密钥
model = OpenAIChatModel(api_key="your_openai_key")
agent = ChatAgent(model=model)

# 简单测试
usr_msg = "Hello, what's the weather today?"
response = agent.step(usr_msg)
print(response.msgs[0].content)
