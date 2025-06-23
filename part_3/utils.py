
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

def load_files_from_config(config: dict) -> dict:
    """根据配置加载所有文件内容"""
    file_contents = {}
    for file_info in config.get("files", []):
        file_path = file_info["path"]
        comment = file_info.get("comment", "")

        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()

            # 使用 CAMEL 的文件处理功能
            file_obj = create_file_from_raw_bytes(file_content, file_path)

            file_contents[file_path] = {
                "content": file_obj.docs[0]["page_content"],
                "comment": comment,
                "type": file_info.get("type", "unknown")
            }
            print("BLACK", f"'{file_path}' read", None, True)
        except Exception as e:
            output("BLACK", f"无法加载文件 {file_path}: {e}", None, True)
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










