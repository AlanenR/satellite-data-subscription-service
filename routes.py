from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/sign-up")
def signUp():
    return render_template("sign-up.html")

@app.route("/admin-panel")
def adminPanel():
    return render_template("admin-panel.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")
