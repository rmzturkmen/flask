# Jinja Templates

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", number1=10, number2=20)


@app.route("/second")
def yeni():
    return render_template("new.html", prepared="Ramazan")


@app.route("/third")
def assignment1():
    return render_template("HTML-table-img-1.html", prepared="Ramazan")


@app.route("/fourth")
def assigment2():
    return render_template("HTML-table-img-2.html", prepared="Ramazan")


@app.route("/fifth")
def assignment3():
    return render_template("HTML-list.html", prepared="Ramazan")


if __name__ == "__main__":
    app.run(debug=True)
