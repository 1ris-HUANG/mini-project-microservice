from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/info')
def get_info():
    return jsonify({"service": "Info-Service", "version": "1.0.0", "status": "Secure"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)