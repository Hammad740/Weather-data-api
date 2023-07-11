from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def example(station, date):
    temp = 23
    return str(temp)


if __name__ == "__main__":
    app.run(debug=True)
