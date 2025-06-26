import os  
import argparse
import sys
import json
from dotenv import load_dotenv  
from camel.loaders import create_file_from_raw_bytes  
from colorama import Fore
from termcolor import colored
from camel.models import ModelFactory  
from camel.types import ModelPlatformType  
from camel.societies import RolePlaying  
from camel.utils import print_text_animated  

def output(color,message,f,std_flag):
    if std_flag:
        #print(repr("Fore."+color)+message)
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
            output("BLACK","\'"+file_path+"\' readed",None,True)
        except Exception as e:  
            print(f"无法加载文件 {file_path}: {e}")
            return {}
      
    return file_contents

def create_roleplay_with_files(json_config_path: str, model, task_prompt: str):  
    # 加载文件配置和内容  
    config = load_file_config(json_config_path)
    output("BLACK","config loaded",None,True)

    file_contents = load_files_from_config(config)
    output("BLACK","file(s) all loaded",None,True)

    if not file_contents:
        print("failed to load file(s) or no input file")
        return None
    # 构建文件信息字符串  
    files_info = "\n".join([  
        f"文件: {path}\n注释: {info['comment']}\n类型: {info['type']}\n内容:\n{info['content']}\n---"  
        for path, info in file_contents.items()  
    ])  
      
    # 为两个代理创建扩展系统消息  
    extend_sys_msg_meta_dicts = [  
        {  
            # Assistant 的扩展信息  
            "assistant_role":"市场营销分析师",
            "user_role":"公司领导层",
            "criteria":(
                f"你可以访问以下文件内容来完成任务：\n{files_info}\n"  
                "请根据文件内容和注释来理解项目结构并提供准确的解决方案。" 
            )
        },  
        {  
            # User 的扩展信息    
            "assistant_role":"市场营销分析师",
            "user_role":"公司领导层",
            "criteria":(
                f"请基于以下文件内容和注释来提出问题和需求：\n{files_info}\n"  
                "注意检查 assistant 的回答是否与实际文件内容一致。" 
            )
        }  
    ]  
    
    output("BLACK","extend_sys_msg_meta_dicts loaded",None,True)

    # 创建 RolePlaying 会话  
    role_play_session = RolePlaying(  
        assistant_role_name="市场营销分析师",  
        assistant_agent_kwargs=dict(model=model),  
        user_role_name="公司领导层",  
        user_agent_kwargs=dict(model=model),  
        task_prompt=task_prompt,  
        with_task_specify=True,
        output_language='中文',
        task_specify_agent_kwargs=dict(model=model),  
        extend_sys_msg_meta_dicts=extend_sys_msg_meta_dicts  
    )  
      
    return role_play_session






def do_roleplay(role_play_session,input_msg,f,std_flag):
    assistant_response, user_response = role_play_session.step(input_msg)  
    if "CAMEL_TASK_DONE" in user_response.msg.content:
        output("RED","TASK_DONE from AI User.",f,std_flag)
        return None
    if  "CAMEL_TASK_DONE" in assistant_response.msg.content:
        output("RED","TASK_DONE from AI Assistant.",f,std_flag)
        return None

    if assistant_response.terminated: 
        output("RED",f"AI Assistant terminated. Reason: {assistant_response.info['termination_reasons']}.",f,std_flag) 
        return None  
            
    if user_response.terminated:  
        output("RED",f"AI User terminated. Reason: {user_response.info['termination_reasons']}.",f,std_flag)
        return None 
            
    # 显示对话内容
    output("BLUE",f"AI User:\n\n{user_response.msgs[0].content}\n",f,std_flag)
    output("GREEN",f"AI Assistant:\n\n{assistant_response.msgs[0].content}\n" ,f,std_flag)
        
    return assistant_response.msgs[0]


def main(args):
    if args.input is None:
        print("No input file")
        return
    if args.output is not None:
        f=open(args.output,'w',encoding="utf-8")
    else:
        f=None
    load_dotenv(dotenv_path='.env')
    api_key = os.getenv('SF_API')
    output("BLACK","SF_API:%s"%(api_key),None,True)

    model = ModelFactory.create(  
        model_platform=ModelPlatformType.SILICONFLOW,  
        model_type="deepseek-ai/DeepSeek-R1", 
        api_key=api_key,
        model_config_dict={
            "temperature":0.7
        }
    )
    output("BLACK","model initialized",None,True)

    task_prompt="进行品牌资产数字化与初步分析，具体内容包括：1. 抓取并解析品牌官网、现有社交媒体内容，提取当前品牌信息传递、内容主题、互动数据、粉丝评论情感；2. 对提供的品牌VI、故事等文档进行NLP分析，提炼核心品牌关键词和价值主张；3.初步评估品牌当前在线声量和情感倾向。" 
    role_play_session = create_roleplay_with_files(  
        json_config_path=args.input,  
        model=model,  
        task_prompt= task_prompt
    )
    output("BLACK","role_play_session initialized",None,True)

    output("GREEN",f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n",f,args.std_flag)
    output("BLUE",f"AI User sys message:\n{role_play_session.user_sys_msg}\n",f,args.std_flag)
    output("YELLOW",f"Original task prompt:\n{task_prompt}\n",f,args.std_flag)
    output("CYAN",f"Specified task prompt:\n{role_play_session.specified_task_prompt}\n",f,args.std_flag)
    output("RED",f"Final task prompt:\n{role_play_session.task_prompt}\n",f,args.std_flag)

    turn_cnt=0
    input_msg=role_play_session.init_chat()
    while turn_cnt < args.limit:
        turn_cnt+=1
        input_msg=do_roleplay(role_play_session,input_msg,f,args.std_flag)
        if input_msg is None:
            break
    return



if __name__ == "__main__": 
    parser=argparse.ArgumentParser(description="示例")
    parser.add_argument("-i","--input",dest="input",help="reference_list.json",required=True)
    parser.add_argument("-o","--output",dest="output",help="output file, default to stdout",default=None)
    parser.add_argument("-s","--std",dest="std_flag",help="1 for stdout, 0 for no stdout. default = 1 when arg -o not given, or 0 when arg -o given",default=None)
    parser.add_argument("-l","--limit",dest="limit",help="chat turn limit",default="50")
    args=parser.parse_args()
    args.limit=int(args.limit)
    if args.std_flag is None:
        args.std_flag = args.output is None
    elif args.std_flag in ["0","1"]:
        args.std_flag = args.std_flag=="1"
    else:
        print("invalid arg: -s --std, only accept '0' or '1'.")
        exit(1)


    main(args)

