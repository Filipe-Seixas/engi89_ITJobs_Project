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


@flask_app.route("/job/<title>")
def table(title):
    jobs_list = dt.load_job(title)
    return render_template("table.html", job=jobs_list)

@flask_app.route("/toprank")
def toprank():
    jobs_list = dt.top_rank1()
    return render_template("toprank.html", jobs=jobs_list)

@flask_app.route("/toplive")
def toplive():
    jobs_list = dt.top_live_jobs1()
    return render_template("toplive.html", jobs=jobs_list)

if __name__ == "__main__":
    flask_app.run(debug=True)

