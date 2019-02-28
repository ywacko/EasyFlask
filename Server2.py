
from flask import Flask,request

app = Flask(__name__)

@app.route("/<question>")
def first(question):
    if question == "hello":
        return "hi there"
    elif question == "name":
        return "Panda"

@app.route("/<questionF>/<questionS>")
def second(questionF, questionS):
    return questionF + " and " + questionS

@app.route("/")
def third():
    question = request.args.get("q1")
    if question == "hello":
        return "hi there"
    elif question == "name":
        return "Panda"

@app.route("/query")
def forth():
    name = request.args.get("name")
    age = request.args.get("age")
    return name + " is " + age + " years old"

if __name__ == '__main__':
    app.run(port=8000)
