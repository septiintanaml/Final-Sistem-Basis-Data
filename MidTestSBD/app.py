from pickle import GET
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return "HomePage"


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
5

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")


app.run()
