from flask import Flask, request, jsonify
from flask_cors import CORS
from main import process_travel_plan
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": [os.getenv("FRONTEND_URL", "http://localhost:3000")],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Accept", "Authorization"],
        "supports_credentials": False
    }
})

# 配置上传文件的存储路径
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'public'))
ALLOWED_EXTENSIONS = {'pdf'}
MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 16 * 1024 * 1024))  # 默认16MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': '没有文件被上传'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': '文件上传成功'}), 200
    
    return jsonify({'error': '不支持的文件类型'}), 400

@app.route('/api/files', methods=['GET'])
def list_files():
    try:
        files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) 
                if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f)) 
                and allowed_file(f)]
        return jsonify({'files': files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 用于存储修改历史的字典
modification_history = {}

@app.route('/update_travel_plan', methods=['POST'])
def update_travel_plan():
    print("收到请求，请求数据:", request.json)  # 添加请求日志
    try:
        # 获取请求数据
        data = request.json
        user_prompt = data.get('message', '')  # 改为与api.py一致的参数名
        session_id = data.get('session_id', 'default')
        
        # 初始化修改历史
        if session_id not in modification_history:
            modification_history[session_id] = []
            
        # 调用处理函数
        result = process_travel_plan(user_prompt)
        
        # 添加到修改历史
        modification_history[session_id].append({
            "prompt": user_prompt,
            "result": result
        })
        
        # 构建响应格式，与api.py保持一致
        response = {
            "reply": result["reply"],
            "status": "success",
            "session_id": session_id
        }
        
        print("准备发送响应:", response)  # 添加响应日志
        return jsonify(response)
    
    except Exception as e:
        print(f"处理请求时发生错误: {str(e)}")  # 添加错误日志
        return jsonify({
            "reply": f"服务器处理请求时发生错误: {str(e)}",
            "status": "error",
            "session_id": data.get('session_id', 'default')
        }), 500

if __name__ == '__main__':
    app.run(
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 6000)),
        debug=os.getenv("FLASK_DEBUG", "1") == "1"
    ) 