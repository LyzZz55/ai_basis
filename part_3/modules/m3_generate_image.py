########################################################################################
# 基于内容日历和VISystem生成图片作为封面or背景
#       基于Gemini API生成符合品牌VI系统的图片
#       支持根据内容日历主题生成封面图或插图
#       集成品牌色彩、字体和图像风格规范
########################################################################################

from dotenv import load_dotenv
import os
from typing import Dict, List, Union, Optional
import json

# Gemini API相关导入
from google import genai
from google.genai import types
from io import BytesIO
from PIL import Image
import base64


from camel.types import ModelPlatformType, ModelType
from camel.toolkits import HumanToolkit
from camel.agents import ChatAgent  
from camel.models import ModelFactory

import logging
# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('ImageGenerator')

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")
SF_API_KEY = os.getenv("FLOW_API")
dpsk_model = ModelFactory.create(
    model_platform=ModelPlatformType.SILICONFLOW,
    model_type='Pro/deepseek-ai/DeepSeek-R1',
    model_config_dict={
        "max_tokens": 8192,
        "temperature": 0.7
    },
    api_key=SF_API_KEY,
)


from PIL import Image, ImageOps
def image_to_color_ascii(image_path, width=100, height=None, inverted=False):
    """将图片转换为彩色 ASCII 字符表示"""
    try:
        # 打开图片
        with Image.open(image_path) as img:
            # 调整图片大小
            if height is None:
                # 保持原始宽高比
                aspect_ratio = img.height / img.width
                height = int(width * aspect_ratio * 0.5)  # 0.5 是为了补偿终端字符的高宽比差异
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            
            # 如果需要反转颜色
            if inverted:
                img = ImageOps.invert(img)
            
            # 用于显示的 ASCII 字符集
            ascii_chars = "@%#*+=-:. "
            
            # 构建彩色 ASCII 字符串
            ascii_str = ''
            pixels = img.getdata()
            
            for y in range(height):
                for x in range(width):
                    # 获取像素位置
                    idx = y * width + x
                    pixel = pixels[idx]
                    
                    # 处理 RGB 或 RGBA 图像
                    if len(pixel) == 4:  # RGBA
                        r, g, b, a = pixel
                        if a < 128:  # 透明像素
                            ascii_str += ' '
                            continue
                    else:  # RGB
                        r, g, b = pixel
                    
                    # 选择 ASCII 字符（基于亮度）
                    brightness = 0.299 * r + 0.587 * g + 0.114 * b
                    char_index = int(brightness / 255 * (len(ascii_chars) - 1))
                    char = ascii_chars[char_index]
                    
                    # 添加彩色转义序列
                    ascii_str += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
                
                ascii_str += '\n'
            
            return ascii_str
    except Exception as e:
        print(f"处理图片时出错: {e}")
        return None

def print_img_to_terminal_through_img_path(img_path: str):
    ascii_img = image_to_color_ascii(img_path)
    if ascii_img:
        print(ascii_img)
    else:
        logger.error("展示图片错误, ascii_img为None")

def save_image(self, image: Image.Image, path: str) -> bool:
        """保存图片到指定路径"""
        try:
            image.save(path)
            logger.info(f"图片已保存至: {path}")
            return True
        except Exception as e:
            logger.error(f"保存图片失败: {e}")
            return False

class ImageGenerator:
    """基于Gemini API和品牌VI系统的图片生成类"""
    
    def __init__(self, vi_system: Dict, model_name: str = "gemini-2.0-flash-preview-image-generation", max_iteration: int = 5):
        """
        初始化图片生成器
        
        参数:
            vi_system: 品牌VI系统字典，包含色彩、图像风格等信息
            model_name: 使用的Gemini模型名称
        """
        self.vi_system = vi_system
        self.model_name = model_name
        self.client = self._init_client()
        self.human_iterater_agent = self._init_human_agent(dpsk_model)
        self.iteration = 0
        self.max_iteration = max_iteration
        logger.info(f"图片生成器初始化完成，使用模型: {model_name}")
    
    def _init_client(self):
        """初始化Gemini API客户端"""
        try:
            return genai.Client(api_key=GEMINI_API_KEY)
        except Exception as e:
            logger.error(f"初始化Gemini客户端失败: {e}")
            raise
    def _init_human_agent(model: str) -> ChatAgent:
        """
        创建并返回一个配置好人类交互工具的静态代理
        
        Args:
            system_message: 系统消息内容
            model: 使用的模型名称
            
        Returns:
            配置好的 ChatAgent 实例
        """
        # 创建带有人类交互工具的工具包
        human_toolkit = HumanToolkit()
        
        return ChatAgent(
            system_message='''
            你是图片生成模块中人类反馈识别Agent
            你读取人类输入
                如果你判断得到人类的表述为（对生成的图片）满意，没有希望修改某部分，则你返回一个'Over'，除此之外你在任何地方不能使用`Over`这个词
                如果你判断得到人类希望修改生成图片，提出了自己的要求，则你返回原图片生成提示词根据人类需求优化后的结果
            ''',
            model=model,
            tools=[*human_toolkit.get_tools()]
        )
    
    def _match_VI_requirement(self, content:str) -> str:
        return f'''
            根据品牌的VI视觉特色生成满足描述的需要的图片
            VI视觉特色: {self.vi_system}
            需求描述: {content}
            '''
    
    def generate_image_from_content(
        self,
        content: str,
        isFullPrompt: bool = False,
        output_path: Optional[str] = "./tmpImg.png"
    ) -> Union[Image.Image, None]:
        """
        根据描述生成图片
        
        参数:
            content_calendar_entry: 内容日历条目，包含主题、描述等信息
            output_path: 图片保存路径，若为None则不保存
        返回:
            生成的图片对象，若失败则返回None
        """
        try:
            # 构建完整提示词
            if isFullPrompt:
                full_prompt = content
            else:
                full_prompt = self._match_VI_requirement(content)
            logger.info(f"生成图片的提示词: {full_prompt}, 图片将输出至：{output_path}")
            
            # 调用Gemini API生成图片
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )
            
            # 处理返回结果
            image = self._process_response(response)
            if image:
                save_image(image, output_path)
                
            return image
            
        except Exception as e:
            logger.error(f"生成图片失败: {e}")
            return None
    
    def iter_generate(self, original_requirement: str, output_path: str = "./tmpImg.png"):
        original_prompt = self._match_VI_requirement(original_requirement)
        
        while self.iteration < self.max_iteration:
            human_input = input("请输入您对于生成图片的反馈或改进需求")
            human_improve_user_msg = f'''
            原始提示词：{original_prompt}
            人类反馈：{human_input}
            '''
            out = self.human_iterater_agent.step(human_improve_user_msg).msgs[0].content
            self.iteration += 1
            if 'Over' in out:
                logger.info("图片生成，Agent判断出人类满意")
                break
            else:
                self.generate_image_from_content(out, True, output_path=output_path+self.iteration)
        
    
    def _process_response(self, response) -> Union[Image.Image, None]:
        """处理Gemini API响应并提取图片"""
        try:
            if not response.candidates:
                logger.warning("API响应中没有候选结果")
                return None
                
            candidate = response.candidates[0]
            for part in candidate.content.parts:
                if part.inline_data is not None:
                    image = Image.open(BytesIO(part.inline_data.data))
                    logger.info(f"成功获取图片，尺寸: {image.size}")
                    return image
                    
            logger.warning("响应中没有图片数据")
            return None
            
        except Exception as e:
            logger.error(f"处理API响应失败: {e}")
            return None
    
    

def generate_img(vi_system: str, img_requirement: str, output_path: str):
    # 初始化图片生成器
    image_gen = ImageGenerator(vi_system=vi_system)
    
    # 生成内容图片
    content_image = image_gen.generate_image_from_content(
        img_requirement,
        output_path=output_path
    )
    
    # 展示图片
    if content_image:
        print_img_to_terminal_through_img_path(output_path)
        
        image_gen.iter_generate(img_requirement)
 
    



