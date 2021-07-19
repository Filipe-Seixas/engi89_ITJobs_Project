from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results/")
def table():
    return render_template("job_results.html")


if __name__ == "__main__":
    app.run(debug=True)
