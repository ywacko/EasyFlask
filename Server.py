
from flask import Flask

app = Flask(__name__)

@app.route("/name")
def name():
    return "Panda"

@app.route("/hello")
def hello():
    return "hi there"


if __name__ == '__main__':
    app.run()