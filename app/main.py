from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello from Flask in Docker and Kubernetes!")

@app.route('/', methods=['GET'])
def home():
    return jsonify(message="You are home")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
