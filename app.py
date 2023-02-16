from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello I have successfully deployed argocd now this time with webhook of jenkins last last time'
