from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Handles incoming SMS and responds to the sender."""
    incoming_msg = request.form.get("Body")  # Get message from user
    print(f"Received message: {incoming_msg}")  # Log the message

    # Create a response
    resp = MessagingResponse()
    resp.message(f"You said: {incoming_msg}")  # Echo user message

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
