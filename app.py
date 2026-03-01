from flask import Flask, jsonify
import datetime
import platform
import random

app = Flask(__name__)

# 增加一些有趣的随机格言
QUOTES = [
    "Simplicity is the soul of efficiency.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Fix the cause, not the symptom.",
    "First, solve the problem. Then, write the code."
]

@app.route('/')
def hello_world():
    # 获取一些有趣的系统信息，体现微服务的环境特征
    info = {
        "message": "🚀 Hello from Python Microservice!",
        "status": "Online",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment": {
            "os": platform.system(),
            "node_name": platform.node(), # 显示容器的 ID，这对 K8s 演示非常有用
            "python_version": platform.python_version()
        },
        "daily_quote": random.choice(QUOTES)
    }
    return jsonify(info)

# 增加一个健康检查接口（这是微服务最佳实践，加分项！）
@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)