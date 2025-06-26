# utils.py
# for alpha ver 1.15.0+ [Main] Agent 2

import ahocorasick
def build_automaton_from_file(wordlist_path="sys_in/sensitive_words.txt"):
    """
    从文件读取敏感词并构建AC自动机。
    """
    # 实例化一个AC自动机
    A = ahocorasick.Automaton()

    # 从文件中读取每个词并添加到自动机中
    try:
        with open(wordlist_path, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip()
                if word:  # 确保行不为空
                    A.add_word(word, word)
    except FileNotFoundError:
        print(f"错误：敏感词库文件 '{wordlist_path}' 未找到。")
        return None
    
    # 构建AC自动机，建立失败指针
    A.make_automaton()
    return A

def contains_sensitive_word(long_text: str, automaton: ahocorasick.Automaton) -> bool:
    """
    使用构建好的AC自动机检查长字符串中是否包含任何敏感词。
    
    参数:
    long_text (str): 需要检查的输入字符串。
    automaton (ahocorasick.Automaton): 预先构建好的AC自动机实例。
    
    返回:
    bool: 如果找到任何敏感词，返回 True；否则返回 False。
    """
    if not automaton:
        print("AC自动机未初始化，无法进行查找。")
        return False
        
    # A.iter() 返回一个迭代器，(end_index, value)
    # 我们只需要知道是否存在匹配，而不需要知道具体是哪个词或在哪里。
    # 所以，只要迭代器能返回第一个值，就说明存在匹配。
    try:
        next(automaton.iter(long_text))
        return True
    except StopIteration:
        # 如果迭代器为空（即没有找到任何匹配），会立即触发StopIteration异常
        return False
    
sensitive_word_automaton = build_automaton_from_file()
def check_sensitive_word(s: str):
    '''true, if has sensitive words'''
    return contains_sensitive_word(s, sensitive_word_automaton)






#########################
import json
from typing import Dict, Any
from termcolor import colored


def output(color,message,f=None,std_flag=1):
    if std_flag:
        print(colored(message,color.lower()))
    if f is not None:
        f.write("--------"+color+"--------\n"
            +message
            +"\n"
        )
    return

def load_file_config(json_path: str) -> Dict[str, Any]:
    """从 JSON 文件加载文件配置"""
    print(f"正在从 '{json_path}' 加载配置文件...")
    with open(json_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

import pandas as pd
from PIL import Image
def load_files_from_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    根据配置加载所有文件内容。
    """
    file_contents = {}
    print("开始根据配置加载输入文件...")

    for file_info in config.get("files", []):
        file_path = file_info["path"]
        comment = file_info.get("comment", "")
        file_type = file_info.get("type", "")
        
        try:
            if file_type == 'text':
                # --- 核心修改：使用标准 Python 读取文件 ---
                # 直接以文本模式（'r'）和 utf-8 编码打开文件
                with open(file_path, 'r', encoding='utf-8') as f:
                    # 读取文件的全部内容为字符串
                    text_content = f.read()

                # 直接将读取到的字符串内容存入字典
                if check_sensitive_word(text_content):
                    output("RED", f"读取到了敏感词!在文本{text_content}中")
                    return {}
                file_contents[comment] = {
                    "content": text_content,  # 直接使用读取到的字符串
                    "path": file_path,
                    "type": file_type
                }
            elif file_type == 'excel':
                 # 读取所有sheet为dict
                excel_data = pd.read_excel(file_path, sheet_name=None, engine="openpyxl")
                # 转为dict（sheet名: 行数据list[dict]）
                excel_dict = {sheet: df.to_dict(orient="records") for sheet, df in excel_data.items()}
                if check_sensitive_word(excel_dict):
                    output("RED", f"读取到了敏感词!在excel解析结果{excel_dict}中")
                    return {}
                file_contents[file_path] = {
                    "content": excel_dict,
                    "comment": comment,
                    "type": file_type
                }
            elif file_type == 'img':
                img = Image.open(file_path)
                file_contents[file_path] = {
                    "content": img.copy(),  # 返回PIL对象副本
                    "comment": comment,
                    "type": file_type
                }
                img.close()
            else:
                output("RED", f"✘ 文件类型不明: {file_path}")
                return {}
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

################



import os

def save_to_file(content: str, *path_parts) -> None:
    """将字符串保存到指定多层路径文件，自动创建文件夹"""
    file_path = os.path.join(*path_parts)
    dir_path = os.path.dirname(file_path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content)
        print(f"内容已追加到文件: {file_path}")
    except Exception as e:
        print(f"写入文件时出错: {e}")


def clean_json_string(s):
    s = s.strip()
    if s.startswith("```json"):
        s = s[len("```json"):].lstrip()
    if s.endswith("```"):
        s = s[:-3].rstrip()
    return s