from flask import Flask,request,jsonify

from common.models.Message import Message
from producer.Producer import Producer

app = Flask(__name__)
producer = Producer()

@app.route('/produce', methods=['POST'])
def produce():
    data = request.get_json()
    try:
        message = Message(
            value=data.get('value'),
            key=data.get('key'),
            timestamp=data.get('timestamp'),
            headers=data.get('headers'),
        )
        message_id = producer.publish_message(message)
        return jsonify({"message_id": message_id}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)