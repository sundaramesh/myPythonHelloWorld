from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Northern Trust - Omnium Team. Greetings from Python World!"
