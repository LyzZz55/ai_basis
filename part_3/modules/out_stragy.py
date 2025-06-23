import os
from dotenv import load_dotenv
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
import json
from typing import Dict, Any, List

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")

# 统一模型工厂，避免重复
def get_model(platform, model_type, api_key, max_tokens=4096, temperature=0.7):
    return ModelFactory.create(
        model_platform=platform,
        model_type=model_type,
        model_config_dict={
            "max_tokens": max_tokens,
            "temperature": temperature
        },
        api_key=api_key,
    )

gemini_model = get_model(
    ModelPlatformType.GEMINI,
    ModelType.GEMINI_2_0_FLASH,
    GEMINI_API_KEY
)
dpsk_model = get_model(
    ModelPlatformType.SILICONFLOW,
    'Pro/deepseek-ai/DeepSeek-R1',
    SF_API_KEY,
    max_tokens=8192
)

class RefinedPublishingStrategyAgent:
    """
    精细化发布策略与主视觉生成Agent
    """
    def __init__(self, vi_system: Dict[str, Any]):
        self.vi_system = vi_system
        self.prompt_agent = ChatAgent(
            system_message="你是社交媒体主视觉AI prompt工程师，负责将内容日历条目和VI系统规范转化为高质量AI图像生成prompt。",
            model=dpsk_model,
            message_window_size=1000,
        )
        # 假设有一个ImageGenerator类用于实际图片生成
        from part_3.modules.m3_generate_image import ImageGenerator
        self.image_generator = ImageGenerator(vi_system=vi_system)

    

    def batch_generate_main_visuals(self, tasks: List[Dict[str, Any]], output_dir: str) -> List[str]:
        """
        批量为内容日历生成主视觉图片，返回图片路径列表
        """
        os.makedirs(output_dir, exist_ok=True)
        results = []
        for idx, task in enumerate(tasks):
            output_path = os.path.join(output_dir, f"main_visual_{idx+1}.png")
            img_path = self.generate_main_visual_for_task(task, output_path)
            results.append(img_path)
        return results

# ================== 测试样例 ==================
if __name__ == "__main__":
    # 假设已获得vi_system和内容日历tasks
    vi_system = {
        "colorPalette": {"primary": {"name": "科技蓝", "hex": "#0055FF"}},
        "imageryStyleGuide": {"photography": {"theme": ["产品", "科技"]}}
    }
    tasks = [
        {
            "platform": "抖音",
            "theme": "小水弹微囊技术全解密",
            "content": "30秒动画《5步看懂干细胞变护肤品》"
        },
        {
            "platform": "小红书",
            "theme": "成分溯源",
            "content": "李媛博士IP直播，现场演示干细胞萃取实验"
        }
    ]
    agent = RefinedPublishingStrategyAgent(vi_system)
    output_dir = "./main_visuals"
    img_paths = agent.batch_generate_main_visuals(tasks, output_dir)
    print("生成的主视觉图片路径：", img_paths)