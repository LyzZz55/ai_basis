# utils.py
# for alpha ver 1.15.0+ [Main] Agent 2

import ahocorasick
import os

def build_automaton_from_file(wordlist_path="sys_in/sensitive-stop-words"):
    """
    从文件或文件夹递归读取敏感词并构建AC自动机。
    - 如果是文件，逐行读取词条；
    - 如果是文件夹，递归读取所有 .txt 文件，合并所有词条。
    """
    A = ahocorasick.Automaton()
    words = set()

    def read_words_from_file(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    word = line.strip()
                    if word:
                        words.add(word)
        except Exception as e:
            print(f"读取敏感词文件 '{file_path}' 时出错: {e}")

    if os.path.isfile(wordlist_path):
        read_words_from_file(wordlist_path)
    elif os.path.isdir(wordlist_path):
        for root, _, files in os.walk(wordlist_path):
            for fname in files:
                if fname.lower().endswith('.txt'):
                    read_words_from_file(os.path.join(root, fname))
    else:
        print(f"错误：敏感词路径 '{wordlist_path}' 不存在。")
        return None

    if not words:
        print(f"警告：敏感词文件为空。")
        return None

    for word in words:
        A.add_word(word, word)
    A.make_automaton()
    return A

def is_english_word(text, start, end):
    """检查是否为英文单词（使用Unicode属性判断）"""
    # 检查匹配部分是否全部是英文字母
    matched_part = text[start:end+1]
    if not all('\u0041' <= c <= '\u005a' or '\u0061' <= c <= '\u007a' for c in matched_part):
        return False
    return True

def is_whole_word_boundary(text, start, end):
    """智能边界检查（仅对英文单词生效）"""
    # 如果不是英文单词，则不检查边界（如中文）
    if not is_english_word(text, start, end):
        return True
    
    # 对英文单词进行边界检查
    # 左边检查：起始位置或前一个字符是非字母和非中文
    left_ok = (start == 0) or (
        not text[start-1].isalpha() and 
        not ('\u4e00' <= text[start-1] <= '\u9fff')  # 非中文
    )
    
    # 右边检查：结束位置或后一个字符是非字母、非中文，允许紧跟标点
    right_ok = (end == len(text)-1) or (
        not text[end+1].isalpha() and 
        not ('\u4e00' <= text[end+1] <= '\u9fff')  # 非中文
    )
    
    return left_ok and right_ok

def contains_sensitive_word(long_text: str, automaton: ahocorasick.Automaton):
    """
    检查长字符串中是否包含任何敏感词，并返回(是否包含, 敏感词列表)。
    """
    if not automaton:
        print("AC自动机未初始化，无法进行查找。")
        return False, []
    found = set()
    for end_index, word in automaton.iter(long_text):
        start_index = end_index - len(word)+1
        if is_whole_word_boundary(long_text, start_index, end_index):
            found.add(word)
    return (len(found) > 0), list(found)
    
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
    if f is not None and (not f.closed):
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

def load_files_from_config(config: Dict[str, Any], f=None,std_flag=1) -> Dict[str, Any]:
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
                output("RED", f"✘ 文件类型不明: {file_path}", f,std_flag)
                return {}
            output("GREEN", f"✔ 已成功加载文件: '{file_path}' ({comment})", f,std_flag)
        except FileNotFoundError:
            output("RED", f"✘ 文件未找到: {file_path}", f,std_flag)
            return {}
        except UnicodeDecodeError:
            output("RED", f"✘ 文件 '{file_path}' 不是有效的 UTF-8 编码，无法解析。", f,std_flag)
            return {}
        except Exception as e:
            output("RED", f"✘ 加载文件 {file_path} 时发生未知错误: {e}", f,std_flag)
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
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"内容已写入到文件: {file_path}")
    except Exception as e:
        print(f"写入文件时出错: {e}")


def clean_json_string(s):
    s = s.strip()
    if s.startswith("```json"):
        s = s[len("```json"):].lstrip()
    if s.endswith("```"):
        s = s[:-3].rstrip()
    return s