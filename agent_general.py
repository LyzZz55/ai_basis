try:
    import utils
except ImportError:
    print("错误：无法从 key.py 导入 API 密钥。")
    print("请创建一个名为 key.py 的文件，并在其中定义变量: key = '您的SiliconFlow_API密钥'")
    exit()

from utils import output
import agent1
import agent2
import agent3
from agent3_modules.Paser import process_and_save_delimited_blocks
from time import time
import argparse

if __name__ == "__main__": 
    main_start_time=time()
    parser=argparse.ArgumentParser(description="示例")
    parser.add_argument("-i","--input",dest="input",help="reference_list.json",required=True)
    parser.add_argument("-o","--output",dest="output",help="output file, default to stdout", default="part1_out.txt")
    parser.add_argument("-s","--std",dest="std_flag",help="1 for stdout, 0 for no stdout. default = 1 when arg -l not given, or 0 when arg -o given",default=None)
    parser.add_argument("-l","--log",dest="log",help="log_output",default=None)
    args=parser.parse_args()
    if args.std_flag is None:
        args.std_flag = args.log is None
    elif args.std_flag in ["0","1"]:
        args.std_flag = args.std_flag=="1"
    else:
        output("BLACK","invalid arg: -s --std, only accept '0' or '1'.",None,True)
        exit(1)

    agent1.main(args)
    agent_1_main_end_time=time()
    output("RED","agent One total time: %d"%(agent_1_main_end_time-main_start_time),None,True)
    # # agent 1 的输出的格式化
    agent_one_out_path = args.output
    process_and_save_delimited_blocks(agent_one_out_path, 3, "outputs", ["Comprehensive_Market_And_Competitor_Intelligence_Report", "Detailed_Target_Audience_Persona_Portfolio", "Brand_Social_Media_Strategic_Playbook"])
    
    # agent 2 
    agent2.main('part2_in/agent2_in.json')
    agent_2_main_end_time=time()
    output("RED","agent Two total time: %d"%(agent_2_main_end_time-agent_1_main_end_time),None,True)
    
    # agent 3
    agent3.perform_part_three(part_3_input_config='part3_in/in.json', parent_out_path='outputs')
    agent_3_main_end_time=time()
    output("RED","agent Three total time: %d"%(agent_3_main_end_time-agent_2_main_end_time),None,True)

    
    