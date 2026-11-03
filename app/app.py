from config import Config
from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    return f"Привет {session.get('who', 'Гость')}"


@app.route("/<username>")
def log(username):
    session["who"] = username
    return redirect("/")
