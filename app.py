# Web applikation
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/salary")
def salary():
    return render_template("salary.html")



@app.route("/hej.html")
def hej():
    return "Hejsan <b>på dig</b>"


@app.route("/")
def hello_world():
    return "<p>Hello, World Stefan!</p>"

app.run()    