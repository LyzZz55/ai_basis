# utils.py
# for alpha ver 1.15.0+ [Main] Agent 2

import json
from typing import Dict, Any


def output(color: str, message: str, f=None, std_flag=None):
    """一个简单的打印函数，用于模拟给定的 output 函数。"""
    color_map = {
        "GREEN": "\033[92m",
        "RED": "\033[91m",
        "END": "\033[0m",
    }
    start_color = color_map.get(color, "")
    end_color = color_map.get("END", "")
    print(f"{start_color}{message}{end_color}")


def load_file_config(json_path: str) -> Dict[str, Any]:
    """从 JSON 文件加载文件配置"""
    print(f"正在从 '{json_path}' 加载配置文件...")
    with open(json_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config


def load_files_from_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    根据配置加载所有文件内容。
    """
    file_contents = {}
    print("开始根据配置加载输入文件...")

    for file_info in config.get("files", []):
        file_path = file_info["path"]
        comment = file_info.get("comment", "")

        try:
            # --- 核心修改：使用标准 Python 读取文件 ---
            # 直接以文本模式（'r'）和 utf-8 编码打开文件
            with open(file_path, 'r', encoding='utf-8') as f:
                # 读取文件的全部内容为字符串
                text_content = f.read()

            # 直接将读取到的字符串内容存入字典
            file_contents[comment] = {
                "content": text_content,  # 直接使用读取到的字符串
                "path": file_path,
                "type": file_info.get("type", "unknown")
            }
            output("GREEN", f"✔ 已成功加载文件: '{file_path}' ({comment})")

        except FileNotFoundError:
            output("RED", f"✘ 文件未找到: {file_path}")
            return {}
        except UnicodeDecodeError:
            output("RED", f"✘ 文件 '{file_path}' 不是有效的 UTF-8 编码，无法解析。")
            return {}
        except Exception as e:
            output("RED", f"✘ 加载文件 {file_path} 时发生未知错误: {e}")
            return {}

    print("✅ 所有输入文件加载完毕。")
    return file_contents