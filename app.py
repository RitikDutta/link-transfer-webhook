from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        return "Webhook received!"
        os.system("xdg-open http://google.com")
        webbrowser.open_new('xdg-open http://google.com')
app.run(host='0.0.0.0', port=8000) 
