from flask import Flask, request
import requests
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from helper import chatbot_response

# Configure application
app = Flask(__name__)


@app.route("/send")
def send():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello, there!',
        to='whatsapp:+14155238886'
    )

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    ret = chatbot_response(incoming_msg)
    msg.body(ret)
    return str(resp)


if __name__ == '__main__':
   app.run()