from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert:", data)  # Log data for debugging
    # Put your trading logic here
    return jsonify({"status": "received", "data": data})

@app.route('/', methods=['GET'])
def home():
    return "Webhook is live!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
