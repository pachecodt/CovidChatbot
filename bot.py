from flask import Flask, request
import requests
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from helper import chatbot_response


GREETING_KEYWORDS = ("olá", "oi", "viva", "boas", "hi")
QUOTES_KEYWORDS = ("quote", "frase", "citação", "citacao")
CATS_KEYWORDS = ("cat", "gato", "gata", "gatinho", "gatinha")

# Configure application
app = Flask(__name__)


@app.route("/send")
def send():
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
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
    responded = False

    if bool([ele for ele in GREETING_KEYWORDS if(ele in incoming_msg)]):
        msg.body("Hi!" + 3 * "\n")
        responded = True

    if bool([ele for ele in QUOTES_KEYWORDS if(ele in incoming_msg)]):
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'Não consegui recuperar uma citação neste momento, desculpe.'
        msg.body(quote)
        responded = True

    if bool([ele for ele in CATS_KEYWORDS if(ele in incoming_msg)]):
        msg.media('https://cataas.com/cat')
        responded = True
    
    if not responded:
        msg.body("Só conheço frases e gatos famosos, desculpe!")
    return str(resp)

@app.route('/bot2', methods=['POST'])
def bot2():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    ret = chatbot_response(incoming_msg)
    msg.body(ret)
    return str(resp)


if __name__ == '__main__':
   app.run()