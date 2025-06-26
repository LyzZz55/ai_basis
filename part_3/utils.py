
import json
from camel.loaders import create_file_from_raw_bytes
from termcolor import colored

import os


def output(color,message,f,std_flag):
    if std_flag:
        print(colored(message,color.lower()))
    else:
        print(message)
        
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
                # print("BLACK", f"'{file_path}' read", None, True)
                
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

def clean_json_string(json_str: str) -> str:
            """清理JSON字符串，移除markdown代码块标记"""
            # 移除 ```json 开头
            if '```json' in json_str:
                json_str = json_str.split('```json')[-1]
            # 移除 ``` 结尾
            if '```' in json_str:
                json_str = json_str.split('```')[0]
            return json_str.strip()










