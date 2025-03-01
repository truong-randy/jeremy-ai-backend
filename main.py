from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Add a simple route for the root path
@app.route("/", methods=['GET'])
def index():
    return "Server is running. Send POST requests to /sms for Twilio integration."

@app.route("/sms", methods=['POST'])
def sms_reply():
    try:
        # Log incoming request for debugging
        logging.info(f"Received message: {request.form}")
        
        # Extract message and phone number
        msg = request.form.get('Body', '')
        phone_number = request.form.get('From', '')
        
        logging.info(f"Message: {msg}, From: {phone_number}")
        
        # Create TwiML response
        resp = MessagingResponse()
        
        # Basic confirmation response
        resp.message(f"Thanks for your message: '{msg}'. We're processing it now.")
        
        # Return valid TwiML response
        return str(resp), 200, {'Content-Type': 'text/xml'}
    except Exception as e:
        # Log any errors
        logging.error(f"Error processing SMS: {str(e)}")
        
        # Still return a valid response even if there's an error
        resp = MessagingResponse()
        resp.message("Sorry, we encountered an issue processing your message.")
        return str(resp), 200, {'Content-Type': 'text/xml'}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10000)

