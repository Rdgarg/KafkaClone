from flask import Flask,request,jsonify

from producer.Producer import Producer

app = Flask(__name__)

@app.route('/publish_message', methods=['POST'])
def publish_message():
    # This is where you would handle the message publishing logic
    # For example, you could extract the message from the request and call the Producer's publish_message method
    producer = Producer()
    print("producer is initialized")
    message = request.json.get('message')
    print("message is {}".format(message))
    message_id = producer.publish_message(message)
    return jsonify({"message_id": message_id})

if __name__ == '__main__':
    app.run(debug=True)