from app import app
from flask import redirect, render_template, request, session
from os import getenv

app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # TODO: check username and password
        session["username"] = username
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/sign-up")
def signUp():
    return render_template("sign-up.html")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/admin-panel")
def adminPanel():
    return render_template("admin-panel.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/data-feed")
def dataFeed():
    return render_template("data-feed.html")
