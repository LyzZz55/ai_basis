import json
import os

KB_DIR = os.path.join(os.path.dirname(__file__), '..', 'knowledge_base')

def fileLoader(kb_name: str) -> dict:
    """
    Loads a specified knowledge base file (e.g., JSON).
    For simplicity, assumes JSON files in the knowledge_base directory.
    """
    # Example kb_name: "platform_characteristics.json"
    file_path = os.path.join(KB_DIR, kb_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # print(f"Knowledge base '{kb_name}' loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: Knowledge base file '{file_path}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{file_path}'.")
        return {}

# Example: Create dummy KB files in a 'knowledge_base' directory
# knowledge_base/platform_characteristics.json:
# {
#   "Weibo": {"peak_times_general": ["10am-12pm", "8pm-10pm"], "ad_formats": ["Feed Ad", "Fan Tunnel"], "max_image_size_kb": 2048},
#   "Xiaohongshu": {"peak_times_general": ["7pm-9pm", "10pm-12am"], "ad_formats": ["Search Ad", "Note Ad"], "cover_aspect_ratio": "3:4"},
#   "Douyin": {"peak_times_general": ["12pm-2pm", "7pm-9pm"], "ad_formats": ["In-Feed Ad", "TopView"], "video_max_duration_s": 60}
# }

# knowledge_base/industry_keywords.json:
# {
#   "Fashion": ["#OOTD", "#StreetStyle", "#NewCollection", "时尚穿搭"],
#   "Tech": ["#Gadgets", "#Innovation", "#FutureTech", "科技新品"]
# }

# knowledge_base/visual_design_principles.json:
# {
#   "color_psychology": {"blue": "trust, stability", "red": "energy, passion"},
#   "layout_theory": {"rule_of_thirds": "...", "golden_ratio": "..."}
# }