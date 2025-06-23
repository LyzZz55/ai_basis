
import json
from camel.loaders import create_file_from_raw_bytes
from termcolor import colored

def save_to_file(content: str, file_path: str,io_pattern = 'a' , encoding: str = 'utf-8') -> None:
    """将string保存到指定文件"""
    try:
        with open(file_path, io_pattern, encoding=encoding) as file:
            file.write(content)
        print(f"内容已追加到文件: {file_path}")
    except Exception as e:
        print(f"写入文件时出错: {e}")

def output(color,message,f,std_flag):
    if std_flag:
        print(colored(message,color.lower()))
    if f is not None:
        f.write("--------"+color+"--------\n"
            +message
            +"\n"
        )
    return

def load_file_config(json_path: str) -> dict:
    """从 JSON 文件加载文件配置"""
    with open(json_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config
from PIL import Image
import base64
import io

def load_files_from_config(config: dict) -> dict:
    """根据配置加载所有文件内容"""
    file_contents = {}
    
    for file_info in config.get("files", []):
        file_path = file_info["path"]
        comment = file_info.get("comment", "")
        file_type = file_info.get("type", "")
        
        try:
            if file_type == 'text':
                with open(file_path, 'rb') as f:
                    file_content = f.read()

                # 使用 CAMEL 的文件处理功能
                file_obj = create_file_from_raw_bytes(file_content, file_path)

                file_contents[file_path] = {
                    "content": file_obj.docs[0]["page_content"],
                    "comment": comment,
                    "type": file_type  # 直接使用已获取的 file_type
                }
                print("BLACK", f"'{file_path}' read", None, True)
                
            elif file_type == 'img':
                # 图片处理逻辑
                with Image.open(file_path) as img:
                    # 调整图片大小（如果需要）
                    max_size = (800, 600)
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                    
                    # 转换为 base64 以便存储或传输
                    buffer = io.BytesIO()
                    img_format = img.format if img.format else 'JPEG'
                    img.save(buffer, format=img_format)
                    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                    
                    # 获取图片尺寸和其他元数据
                    width, height = img.size
                    
                    file_contents[file_path] = {
                        "content": img_base64,
                        "comment": comment,
                        "type": file_type,
                        "metadata": {
                            "width": width,
                            "height": height,
                            "format": img_format,
                            "size_kb": len(img_base64) * 3/4 / 1024  # 估算 KB
                        }
                    }
                    print("BLACK", f"'{file_path}' processed as image", None, True)
                    
            else:
                print("YELLOW", f"未知文件类型: {file_type}，跳过文件 {file_path}", None, True)
                continue
                
        except FileNotFoundError:
            print("RED", f"文件不存在: {file_path}", None, True)
        except PermissionError:
            print("RED", f"无权限访问文件: {file_path}", None, True)
        except Exception as e:
            print("RED", f"处理文件 {file_path} 时出错: {str(e)}", None, True)
            return {}
            
    return file_contents    

import logging
def setup_logger(logger_name: str, log_file_path: str = 'image_generator.log') -> logging.Logger:
    """
    配置日志系统，同时输出到终端和文件
    
    Args:
        log_file_path: 日志文件路径，默认为 'image_generator.log'
        
    Returns:
        配置好的 Logger 实例
    """
    # 创建名为 'ImageGenerator' 的日志器
    logger = logging.getLogger(logger_name)
    
    # 确保日志器没有重复的处理器
    if not logger.handlers:
        # 设置日志级别
        logger.setLevel(logging.INFO)
        
        # 创建格式化器
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # 创建并配置文件处理器
        file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        
        # 创建并配置流处理器（输出到终端）
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)
        
        # 将处理器添加到日志器
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    
    return logger




def clean_json_string(json_str: str) -> str:
            """清理JSON字符串，移除markdown代码块标记"""
            # 移除 ```json 开头
            if '```json' in json_str:
                json_str = json_str.split('```json')[-1]
            # 移除 ``` 结尾
            if '```' in json_str:
                json_str = json_str.split('```')[0]
            return json_str.strip()










