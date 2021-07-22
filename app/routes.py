from flask import Flask, render_template
from app import flask_app
import sqlite3
from app.database import Database

dt = Database()


@flask_app.route("/index")
@flask_app.route("/")
def index():
    jobs_list = dt.get_jobs()
    return render_template("index.html", jobs=jobs_list)


@flask_app.route("/job/")
def table():
    jobs_list = dt.all_data()
    return render_template("table.html", jobs=jobs_list)


if __name__ == "__main__":
    flask_app.run(debug=True)