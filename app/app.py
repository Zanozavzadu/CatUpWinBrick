from config import Config
from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    if "username" not in session:
        return redirect("/registration")
    return render_template("start.html", username=session["username"])


@app.route("/registration", methods=["GET", "POST"])
def registration():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username
        return redirect("/")

    return render_template("reg.html")
