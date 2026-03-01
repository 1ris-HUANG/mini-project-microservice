from flask import Flask, jsonify
import datetime
import platform
import random
import requests

# add some interesting quotes
QUOTES = [
    "Simplicity is the soul of efficiency.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Fix the cause, not the symptom.",
    "First, solve the problem. Then, write the code."
]

@app.route('/')
def hello_world():
    # get some info,show the characteristics of a Microservices Environment
    info = {
        "message": "🚀 Hello from Python Microservice!",
        "status": "Online",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment": {
            "os": platform.system(),
            "node_name": platform.node(), # Display the container ID, which is very useful for K8s demonstrations.
            "python_version": platform.python_version()
        },
        "daily_quote": random.choice(QUOTES)
    }
    return jsonify(info)

# Add a health check interface
@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


    @app.route('/')
def hello():
    try:
        resp = requests.get("http://info-service/info")
        info_data = resp.json()
    except:
        info_data = "Info-Service unreachable"

    # Include the retrieved information in the returned JSON
    # Return the previous JSON + info_data
app = Flask(__name__)