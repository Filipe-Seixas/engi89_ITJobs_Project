from flask import Flask, render_template, Response
from app import flask_app
import sqlite3
from app.database import Database
from flask import send_file

dt = Database()


@flask_app.route("/index")
@flask_app.route("/")
def index():
    jobs_list = dt.get_jobs()
    return render_template("index.html", jobs=jobs_list)


@flask_app.route("/job/<title>")
def table(title):
    jobs_list = dt.load_job(title)
    return render_template("table.html", job=jobs_list, title=title)

@flask_app.route("/toprank")
def toprank():
    jobs_list = dt.top_rank1()
    return render_template("toprank.html", jobs=jobs_list)

@flask_app.route("/toplive")
def toplive():
    jobs_list = dt.top_live_jobs1()
    return render_template("toplive.html", jobs=jobs_list)

# @flask_app.route("/download")
# def home():
#     return render_template("download.html")

@flask_app.route("/download")
def download_file():
    p = "job_ranks.csv"
    return send_file(p,as_attachment=True)

@flask_app.route("/download2")
def download_file_2():
    p2 = "live_jobs.csv"
    return send_file(p2,as_attachment=True)

@flask_app.route("/download3/<title>")
def download_file_3(title):
    p3 = "job.csv"
    print(title)
    return send_file(p3,as_attachment=True, attachment_filename = title + ".csv")

if __name__ == "__main__":
    flask_app.run(debug=True)

