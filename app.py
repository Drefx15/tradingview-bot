from flask import Flask, request
import logging

app = Flask(__name__)

# Set up logging to display messages in Render logs
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    logging.info(f"✅ Webhook received: {data}")
    return '', 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
