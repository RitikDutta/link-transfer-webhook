from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        url = request.json['message']
        url = url.replace("'", "")
        command = "xdg-open {}".format(url)
        print("URL = ", command)
        os.system(command)
        return "Webhook received!"
app.run(host='0.0.0.0', port=8000) 
