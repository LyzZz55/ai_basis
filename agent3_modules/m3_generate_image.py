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

from utils import output

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
agent = ChatAgent(
    model=dpsk_model,   
    system_message="""
你是一名资深文生图提示词大师， 根据内容日历条目生成英文提示词，无需解释。

例子：
任务条目：{'task_name': '7月抖音干细胞科普动画制作', 'task_description': "制作30秒动画《5步看懂干细胞变护肤品》，配'微囊不是魔法，是慢释放小水弹'标语，植入会员注册入口，目标完播率≥65%", 'platform': '抖音', 'time': '7月2日', 'theme': '植物干细胞科普周'}
VI系统摘要：{'brandName': 'EcoGarden', 'brandSlogan': None, 'coreValues': ['科技自然', '透明可信', '简约高效'], 'coreElements': ['植物干细胞', '可持续发展'], 'logo': {'description': '抽象化的植物叶脉或细胞结构与几何线条或科技元素相结合，简洁现代', 'mainColor': '#a7d1ab', 'secondaryColors': ['#f5f5dc', '#d3d3d3', '#808080', '亮绿色', '金色'], 'font': {'primary': '现代感强、易读性高的无衬线字体', 'secondary': '衬线字体'}, 'variations': ['不同尺寸', '不同版本', '动画版本']}, 'colorPalette': {'mainColor': '#a7d1ab', 'secondaryColors': ['#f5f5dc', '#d3d3d3', '#808080'], 'accentColors': ['亮绿色', '金色'], 'platformAdjustment': '根据平台差异，适度调整色彩饱和度和亮度'}, 'layoutSystem': {'designPrinciple': '模块化设计，例如成分卡片、技术卡片、环保数据卡片等', 'whitespace': '充分利用留白，清晰划分信息层级，确保易读性和视觉舒适度'}, 'platformStrategies': {'Douyin': '强调动感和视觉冲击', 'Xiaohongshu': '注重生活化和用户生成内容', 'Instagram': '保持高度视觉一致性'}, 'ARVRApplications': {'AR': '产品成分溯源和碳足迹追踪的可视化', 'VR': '微距摄影或3D动画展现植物干细胞的科技感'}, 'userExperience': {'principles': ['易用性', '一致性', '可访问性'], 'testing': '建议进行用户测试以确保设计方案的有效性'}, 'iteration': '持续关注市场趋势，并根据用户反馈不断迭代优化VI系统，确保其长期有效性'}

输出：Visual Style:

Adopt a mixed style of 3D cartoon + flat design, blending sci-tech aesthetics with biological natural elements to suit TikTok's young audience.
Showcase dynamic previews of microcapsule release as fluid animations, implying the "slow-release" concept to enhance visual appeal.

Core Element Composition:

Central Visual:
A giant transparent microcapsule sphere (semi-transparent white with light blue gradient) as the main body, containing fluorescent green plant stem cell particles inside (resembling water bomb texture), with particles slowly releasing in dynamic light effects.
The microcapsule is surrounded by vector illustrations of plant stems and leaves (e.g., buds, leaf veins) to emphasize the "plant stem cell" theme.
Process Hints:
Five floating mini circular icons around the microcapsule, each representing the 5 steps ("extraction → cultivation → encapsulation → penetration → skincare") with simple line drawings (e.g., microscope, petri dish, capsule, skin texture), forming a circular motion path to guide the viewer's gaze.
Interactive Elements:
A gradient registration button (blue-purple gradient + white border) floats in the lower right corner, with the text "Unlock Stem Cell Secrets" and a membership icon (key/gift box shape), surrounded by a breathing light effect.

Color and Lighting:

Primary tones: tech blue (#1E88E5) + life green (#43A047) gradient, with a light gray transparent grid background simulating lab petri dish texture.
Light effects: golden particle trails for microcapsule releases, soft glows outlining plant elements to enhance three-dimensionality.

Slogan Presentation:

The slogan "Microcapsules aren’t magic—they’re slow-release water bombs" is displayed above the microcapsule in handwritten typography, with font colors matching the microcapsule gradient, and a water drop emoji (💦) at the end to reinforce the "water bomb" association.

TikTok Scene Adaptation:

    """
)


def generate_visual_prompt(task, vi_system) -> str:
    """
    根据内容日历条目和VI系统，生成主视觉prompt
    """
    prompt = f"""
请根据以下任务条目和品牌VI系统，为该内容生成一条prompt， 用来生成这个任务的主视觉，要求：
- 适当遵循品牌VI系统的色彩、字体、图像风格等规范
- 语言简洁、具体，能够直接输入文生图模型
- 输出仅包含英文prompt，无需解释

任务条目，即需要生产主视觉图片的任务：
{json.dumps(task, ensure_ascii=False)}

品牌VI系统摘要：
{json.dumps(vi_system, ensure_ascii=False)}
9:16 vertical composition, with key elements concentrated in the upper-middle screen (avoiding obstruction by TikTok's bottom interactive bar).
The microcapsule animation preview reflects the fast pace of a "30-second video," with arrow animations suggesting time flow (e.g., a left-to-right timeline light band).


"""
    return prompt

def generate_main_visual_for_task_prompt(task, vi_system) -> str:
        """
        为单个内容日历条目生成主视觉图片，并返回图片路径
        """
        prompt = generate_visual_prompt(task, vi_system)
        # 1. 生成英文prompt
        response = agent.step(prompt)
        ai_prompt = response.msgs[0].content.strip()
        return ai_prompt

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
        output("RED", "展示图片错误, ascii_img为None", None, False)

def save_image(image: Image.Image, path: str) -> bool:
        """保存图片到指定路径"""
        try:
            image.save(path)
            output("BLACK", f"图片已保存至: {path}", None, False)
            return True
        except Exception as e:
            output("RED", f"保存图片失败: {e}", None, False)
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
        output("BLACK", f"图片生成器初始化完成，使用模型: {model_name}", None, False)
    
    def _init_client(self):
        """初始化Gemini API客户端"""
        try:
            return genai.Client(api_key=GEMINI_API_KEY)
        except Exception as e:
            output("RED", f"初始化Gemini客户端失败: {e}", None, False)
            raise
    def _init_human_agent(self, model: str) -> ChatAgent:
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
        
        Args:
            content_calendar_entry: 内容日历条目，包含主题、描述等信息
            output_path: 图片保存路径，若为None则不保存
        Return:
            生成的图片对象，若失败则返回None
        """
        try:
            # 构建完整提示词
            if isFullPrompt:
                full_prompt = content
            else:
                full_prompt = self._match_VI_requirement(content)
            output("BLACK", f"生成图片的提示词: {full_prompt}, 图片将输出至：{output_path}", None, False)
            
            # 调用Gemini API生成图片
            output("GREY", "生成图片 start")
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )
            output("GREY", "生成图片 end")
            
            # 处理返回结果
            image = self._process_response(response)
            if image:
                save_image(image, output_path)
                
            return image
            
        except Exception as e:
            output("RED", f"生成图片失败: {e}", None, False)
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
                output("BLACK", "图片生成，Agent判断出人类满意", None, False)
                break
            else:
                self.generate_image_from_content(out, True, output_path=output_path+self.iteration + ".png")
        
    
    def _process_response(self, response) -> Union[Image.Image, None]:
        """处理Gemini API响应并提取图片"""
        try:
            if not response.candidates:
                output("RED", "API响应中没有候选结果", None, False)
                return None
                
            candidate = response.candidates[0]
            for part in candidate.content.parts:
                if part.inline_data is not None:
                    image = Image.open(BytesIO(part.inline_data.data))
                    output("BLACK", f"成功获取图片，尺寸: {image.size}", None, False)
                    return image
                    
            output("BLACK", "响应中没有图片数据", None, False)
            return None
            
        except Exception as e:
            output("RED", f"处理API响应失败: {e}", None, False)
            return None
    
    

def generate_img(vi_system: str, img_requirement: str, output_path: str):
    # 初始化图片生成器
    image_gen = ImageGenerator(vi_system=vi_system)
    
    # 生成内容图片
    output("GREY", "图片生成器 start")
    content_image = image_gen.generate_image_from_content(
        img_requirement,
        output_path=output_path + ".png"
    )
    output("GREY", "图片生成器 接受数据")
    
    # 展示图片
    if content_image:
        print_img_to_terminal_through_img_path(output_path)
        image_gen.iter_generate(img_requirement)
    output("GREY", "图片生成器 end")
    
 
    



