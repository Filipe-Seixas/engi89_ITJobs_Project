from flask import Flask, render_template
from app import flask_app

@flask_app.route("/")
def home():
    return render_template("home.html")


@flask_app.route("/job/")
def table():
    return render_template("table.html")


if __name__ == "__main__":
    flask_app.run(debug=True)