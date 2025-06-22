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

import logging
# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('ImageGenerator')

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")

class ImageGenerator:
    """基于Gemini API和品牌VI系统的图片生成类"""
    
    def __init__(self, vi_system: Dict, model_name: str = "gemini-2.0-flash-preview-image-generation"):
        """
        初始化图片生成器
        
        参数:
            vi_system: 品牌VI系统字典，包含色彩、图像风格等信息
            model_name: 使用的Gemini模型名称
        """
        self.vi_system = vi_system
        self.model_name = model_name
        self.client = self._init_client()
        logger.info(f"图片生成器初始化完成，使用模型: {model_name}")
    
    def _init_client(self):
        """初始化Gemini API客户端"""
        try:
            return genai.Client(api_key=GEMINI_API_KEY)
        except Exception as e:
            logger.error(f"初始化Gemini客户端失败: {e}")
            raise
    
    def _get_vi_prompt_prefix(self) -> str:
        """从VI系统生成品牌风格提示词前缀"""
        try:
            # 从VI系统获取品牌色彩
            primary_color = self.vi_system.get("color_palette_system", {}).get("primary_colors", ["#000000"])[0]
            secondary_color = self.vi_system.get("color_palette_system", {}).get("secondary_colors", ["#FFFFFF"])[0]
            
            # 获取图像风格
            image_style = self.vi_system.get("imagery_style_guide", {}).get("photography_style", {}).get("overall_mood", "现代简约")
            
            # 生成品牌风格提示词
            return f"品牌风格: {image_style}, 主色调: {primary_color}, 辅助色: {secondary_color}, "
        except Exception as e:
            logger.warning(f"从VI系统获取风格信息失败: {e}")
            return "品牌风格: 现代简约, 主色调: #0070F3, 辅助色: #FFFFFF, "
    
    def generate_image_from_content_calendar(
        self,
        content_calendar_entry: Dict,
        output_path: Optional[str] = None
    ) -> Union[Image.Image, None]:
        """
        根据内容日历条目生成图片
        
        参数:
            content_calendar_entry: 内容日历条目，包含主题、描述等信息
            image_size: 图片尺寸，格式为"宽度x高度"
            quality: 图片质量，可选"high", "medium", "low"
            output_path: 图片保存路径，若为None则不保存
            
        返回:
            生成的图片对象，若失败则返回None
        """
        try:
            # 构建完整提示词
            prompt_prefix = self._get_vi_prompt_prefix()
            content_theme = content_calendar_entry.get("theme", "默认主题")
            content_description = content_calendar_entry.get("description", "")
            
            full_prompt = f"{prompt_prefix} 主题: {content_theme}, 描述: {content_description}"
            logger.info(f"生成图片提示词: {full_prompt}")
            
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
            if image and output_path:
                self.save_image(image, output_path)
            return image
            
        except Exception as e:
            logger.error(f"生成图片失败: {e}")
            return None
    
    def generate_cover_image(
        self,
        title: str,
        subtitle: Optional[str] = None,
        category: Optional[str] = None,
        output_path: Optional[str] = None
    ) -> Union[Image.Image, None]:
        """
        生成封面图片
        
        参数:
            title: 封面标题
            subtitle: 副标题
            category: 内容类别
            output_path: 图片保存路径，若为None则不保存
            
        返回:
            生成的封面图片对象，若失败则返回None
        """
        try:
            # 构建封面图片提示词
            prompt_prefix = self._get_vi_prompt_prefix()
            category_desc = f"类别: {category}, " if category else ""
            subtitle_desc = f"副标题: {subtitle}, " if subtitle else ""
            
            full_prompt = f"{prompt_prefix} 封面标题: {title}, {category_desc}{subtitle_desc} 设计风格: 适合社交媒体封面"
            logger.info(f"生成封面图片提示词: {full_prompt}")
            
            # 调用Gemini API生成图片
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE'],
                )
            )
            
            # 处理返回结果
            image = self._process_response(response)
            if image and output_path:
                self.save_image(image, output_path)
            return image
            
        except Exception as e:
            logger.error(f"生成封面图片失败: {e}")
            return None
    
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
    
    def save_image(self, image: Image.Image, path: str) -> bool:
        """保存图片到指定路径"""
        try:
            image.save(path)
            logger.info(f"图片已保存至: {path}")
            return True
        except Exception as e:
            logger.error(f"保存图片失败: {e}")
            return False
    
    def generate_images_for_calendar(
        self,
        content_calendar: List[Dict],
        output_dir: str = "generated_images",
        image_size: str = "1024x1024",
        quality: str = "high"
    ) -> List[Dict]:
        """
        为内容日历批量生成图片
        
        参数:
            content_calendar: 内容日历列表
            output_dir: 图片保存目录
            image_size: 图片尺寸
            quality: 图片质量
            
        返回:
            生成结果列表，包含图片路径和状态
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        results = []
        for i, entry in enumerate(content_calendar):
            entry_title = entry.get("title", f"entry_{i}")
            safe_title = ''.join(e for e in entry_title if e.isalnum() or e in "._- ")
            output_path = os.path.join(output_dir, f"{safe_title}.png")
            
            image = self.generate_image_from_content_calendar(
                entry,
                image_size=image_size,
                quality=quality,
                output_path=output_path
            )
            
            results.append({
                "entry_id": entry.get("id", i),
                "title": entry_title,
                "image_path": output_path if os.path.exists(output_path) else None,
                "success": image is not None
            })
            
        return results


# ------------------------- 使用示例 -------------------------
if __name__ == "__main__":
    # 示例VI系统（实际应从VI系统生成类获取）
    sample_vi_system = {
        "color_palette_system": {
            "primary_colors": ["#0A7AFF"],
            "secondary_colors": ["#FFD60A", "#4CAF50"],
            "psychology_notes": "蓝色代表科技与信任，黄色代表活力，绿色代表自然"
        },
        "imagery_style_guide": {
            "photography_style": {
                "overall_mood": "现代、简洁、科技感",
                "subject_matter": "产品特写与生活化场景结合"
            }
        }
    }
    
    # 初始化图片生成器
    image_gen = ImageGenerator(vi_system=sample_vi_system)
    
    # 示例内容日历条目
    content_entry = {
        "id": "post_20250620",
        "theme": "夏季新品发布会",
        "description": "展示2025夏季最新产品系列，包含智能手表和无线耳机",
        "title": "2025夏季新品发布会"
    }
    
    # 生成内容图片
    content_image = image_gen.generate_image_from_content_calendar(
        content_entry,
        output_path="summer_products.png"
    )
    
    if content_image:
        content_image.show()
    
    # 生成封面图片
    cover_image = image_gen.generate_cover_image(
        title="2025夏季新品发布会",
        subtitle="智能科技，引领未来",
        category="科技产品",
        output_path="summer_launch_cover.png"
    )
    
    if cover_image:
        cover_image.show()





