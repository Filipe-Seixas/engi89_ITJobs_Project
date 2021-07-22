from app import flask_app
from flask import render_template, flash, redirect, url_for, session


@flask_app.route('/index')
@flask_app.route('/')
def index():
    return render_template('index.html', title='Home')


@flask_app.route('/jobname_results')
def results():
    return render_template('job_results.html', title='Jobname')
