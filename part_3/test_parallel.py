import concurrent.futures
import time
from datetime import datetime

# ========== 函数A：调用Agent生成JSON ==========
def function_a(task_id: int, prompt: str):
    """
    函数A：调用Agent生成JSON数据并输出
    
    Args:
        task_id: 任务ID
        prompt: 提示词
    """
    print(f"🚀 [{datetime.now().strftime('%H:%M:%S')}] Function A started - Task {task_id}")
    
    # 调用Agent的逻辑（实际应用中替换为真实的Agent调用）
    time.sleep(2)  # 模拟Agent调用延迟
    json_data = {"agent": "A", "task_id": task_id, "prompt": prompt}
    
    # 保存JSON文件的逻辑（实际应用中替换为真实的文件操作）
    file_path = f"output_a_{task_id}.json"
    with open(file_path, "w") as f:
        f.write(str(json_data))
    
    # 输出到终端
    print(f"\n===== FUNCTION A RESULT (Task {task_id}) =====")
    print(json_data)
    print("=" * 50)
    
    return {"status": "success", "file_path": file_path}

# ========== 函数B：调用另一个Agent生成JSON ==========
def function_b(task_id: int, prompt: str):
    """
    函数B：调用另一个Agent生成JSON数据并输出
    
    Args:
        task_id: 任务ID
        prompt: 提示词
    """
    print(f"🚀 [{datetime.now().strftime('%H:%M:%S')}] Function B started - Task {task_id}")
    
    # 调用Agent的逻辑（实际应用中替换为真实的Agent调用）
    time.sleep(3)  # 模拟Agent调用延迟
    json_data = {"agent": "B", "task_id": task_id, "prompt": prompt}
    
    # 保存JSON文件的逻辑（实际应用中替换为真实的文件操作）
    file_path = f"output_b_{task_id}.json"
    with open(file_path, "w") as f:
        f.write(str(json_data))
    
    # 输出到终端
    print(f"\n===== FUNCTION B RESULT (Task {task_id}) =====")
    print(json_data)
    print("=" * 50)
    
    return {"status": "success", "file_path": file_path}

# ========== 主程序：并行执行函数A和函数B ==========
def main():
    start_time = time.time()
    print(f"🚀 Workflow started at {datetime.now().strftime('%H:%M:%S')}")
    
    # 配置任务
    tasks = [
        {"id": 1, "prompt": "Generate product description"},
        {"id": 2, "prompt": "Analyze market trends"},
        {"id": 3, "prompt": "Create user profile"}
    ]
    
    # 使用线程池并行执行函数A和函数B
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        # 提交函数A的所有任务
        futures_a = [executor.submit(function_a, task["id"], task["prompt"]) for task in tasks]
        
        # 提交函数B的所有任务
        futures_b = [executor.submit(function_b, task["id"], task["prompt"]) for task in tasks]
        
        # 等待所有任务完成
        concurrent.futures.wait(futures_a + futures_b)
    
    # 汇总结果
    total_time = time.time() - start_time
    print(f"\n🎉 Workflow completed in {total_time:.2f} seconds")

if __name__ == "__main__":
    main()