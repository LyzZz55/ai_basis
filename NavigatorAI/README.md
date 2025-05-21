# NavigatorAI

> 一个基于多智能体框架的智能旅行规划助手，可与用户进行对话生成精美的旅游出行方案，此外可以识别用户在PDF上的标注修改并自动优化旅行方案

由 [Tsumugii24](https://github.com/Tsumugii24) 开发维护

## 项目介绍

NavigatorAI 是一个基于多智能体框架搭建的智能旅行规划助手，能够理解用户对现有旅行计划的反馈和标注，并据此自动调整和优化旅行方案。用户可以在PDF文档上进行批注、画圈或添加文字等方式提出修改建议，系统能够智能识别并生成更新后的旅行计划。

## 功能特点

- 📝 识别PDF上的用户批注和反馈
- 🔄 根据反馈自动调整旅行计划内容
- 📊 生成美观的HTML格式旅行方案
- 📄 支持PDF文件的上传和预览
- 💬 交互式反馈修改流程
- 🌐 前后端分离架构

## 技术栈

### 前端
- Next.js 14
- React 18
- TailwindCSS
- Radix UI 组件库

### 后端
- Python 3.10+
- Flask 3.0.3
- OpenAI API (使用 GPT-4o 等多模态能力的大语言模型)
- Qwen API (调用Qwen2.5-72B-Instruct)
- PDF处理工具链

## 快速开始

### 环境准备

1. 确保已安装 Node.js (18+) 和 Python 3.10+
2. 克隆项目仓库

### 后端设置

1. 进入后端目录
```bash
cd backend
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 创建环境变量文件
```bash
cp .env.example .env
```

4. 在 `.env` 文件中填入必要配置，包括 OpenAI API KEY, OPENAI BASE URL, QWEN API KEY

5. 启动后端服务
```bash
python app.py
```

### 前端设置

1. 进入前端目录
```bash
cd frontend
```

2. 安装依赖
```bash
npm install
```

3. 创建环境变量文件
```bash
cp .env.example .env
```

4. 启动开发服务器
```bash
npm run dev
```

## 使用流程

1. 在前端界面上传旅行计划的 PDF 文件
2. 查看并确认上传的文件
3. 在提示框中输入您希望对旅行计划进行的修改建议
4. 系统会分析您的反馈并生成修改后的方案
5. 您可以下载更新后的 PDF 文件或继续提供新的反馈

## 项目核心结构

```
NavigatorAI/
├── frontend/              # 前端目录
│   ├── app/               # Next.js 应用程序
│   ├── components/        # React 组件
│   ├── styles/            # 样式文件
│   └── public/            # 静态资源和上传的文件
│
├── backend/               # 后端目录
│   ├── app.py             # Flask 应用入口
│   ├── main.py            # 主要业务逻辑
│   ├── pdf2image.py       # PDF处理工具
│   └── html2pdf.py        # HTML转PDF工具
```

## 贡献指南

欢迎提交问题报告、功能请求的issue或直接提交 Pull Requests 来改进项目。

## 许可证

**特别注意**：NavigatorAI遵循[CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/)协议，仅供学习使用，不能商用！！！

---

正在持续迭代中，欢迎反馈问题