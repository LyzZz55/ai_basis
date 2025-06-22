
import json
from camel.loaders import create_file_from_raw_bytes

def save_to_file(content: str, file_path: str,io_pattern = 'a' , encoding: str = 'utf-8') -> None:
    """将string保存到指定文件"""
    try:
        with open(file_path, io_pattern, encoding=encoding) as file:
            file.write(content)
        print(f"内容已追加到文件: {file_path}")
    except Exception as e:
        print(f"写入文件时出错: {e}")

def output(color, message, f, std_flag):
    # if std_flag:
        # print(colored(message, color.lower())) # TODO
    if f is not None:
        f.write("----------" + color + "--------\n" + message + "\n")
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

'''
def write_social_media_vi_guide(data: dict, filename: str = "Social_Media_Visual_Identity_System_Guide.pdf") -> None:
    """
    生成社交媒体视觉识别系统指南PDF
    """
    print(f"Placeholder: Generating PDF '{filename}' with data...")
    # In a real implementation, you'd use a PDF library here.
    # For now, let's save as a simple text file to demonstrate data flow.
    output_path = os.path.join("outputs", filename.replace(".pdf", ".txt"))
    os.makedirs("outputs", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(data))
    print(f"Data for '{filename}' saved to '{output_path}' (as .txt)")


def write_ai_prototypes(data: dict, filename: str = "AI_Assisted_Visual_Prototypes_Package.zip") -> None:
    """
    生成视觉的草稿
    """
    print(f"Placeholder: Generating ZIP '{filename}' with AI prototyping prompts/data...")
    output_path = os.path.join("outputs", filename.replace(".zip", ".txt"))
    os.makedirs("outputs", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(data)) # data would be the prompts package from module 5
    print(f"Data for '{filename}' saved to '{output_path}' (as .txt)")


def write_master_editorial_calendar_v2(data: dict, filename: str = "Master_Editorial_Calendar_V2_With_Visual_Directives.xlsx") -> None:
    """
    生成更新后的任务日历
    """
    print(f"Placeholder: Generating Excel '{filename}' with updated calendar data...")
    output_path = os.path.join("outputs", filename.replace(".xlsx", ".txt"))
    os.makedirs("outputs", exist_ok=True)
    # Data here would be the original calendar enriched with visual directives.
    # For simplicity, assuming data is the enrichment part.
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(data))
    print(f"Data for '{filename}' saved to '{output_path}' (as .txt)")


def write_refined_distribution_strategy(data: dict, filename: str = "Refined_Distribution_And_Engagement_Strategy.docx") -> None:
    """
    生成分发策略
    """
    print(f"Placeholder: Generating DOCX '{filename}' with distribution strategy data...")
    output_path = os.path.join("outputs", filename.replace(".docx", ".txt"))
    os.makedirs("outputs", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(data)) # data is the output from module 7
    print(f"Data for '{filename}' saved to '{output_path}' (as .txt)")


def write_comprehensive_kpi_framework(data: dict, filename: str = "Comprehensive_KPI_Framework_And_Reporting_Template.xlsx") -> None:
    """
    生成KPI报告
    """
    print(f"Placeholder: Generating Excel '{filename}' with KPI framework data...")
    output_path = os.path.join("outputs", filename.replace(".xlsx", ".txt"))
    os.makedirs("outputs", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(data)) # data is the output from module 8
    print(f"Data for '{filename}' saved to '{output_path}' (as .txt)")

import os # ensure os is imported for path operations

'''



def clean_json_string(json_str: str) -> str:
            """清理JSON字符串，移除markdown代码块标记"""
            # 移除 ```json 开头
            if '```json' in json_str:
                json_str = json_str.split('```json')[-1]
            # 移除 ``` 结尾
            if '```' in json_str:
                json_str = json_str.split('```')[0]
            return json_str.strip()










