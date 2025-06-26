try:
    import utils
except ImportError:
    print("错误：无法从 key.py 导入 API 密钥。")
    print("请创建一个名为 key.py 的文件，并在其中定义变量: key = '您的SiliconFlow_API密钥'")
    exit()

from utils import output
import agent1

from time import time
import argparse






if __name__ == "__main__": 
    main_start_time=time()
    parser=argparse.ArgumentParser(description="示例")
    parser.add_argument("-i","--input",dest="input",help="reference_list.json",required=True)
    parser.add_argument("-o","--output",dest="output",help="output file, default to stdout",required=True)
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
    
    
    


    