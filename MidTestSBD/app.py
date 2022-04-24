from pickle import GET
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "HomePage"

@app.route("/login", ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")


app.run()