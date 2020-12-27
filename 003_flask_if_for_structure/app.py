from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def head():
    return render_template("index.html", ramazan=True)


@app.route("/for")
def for_example():
    names = ['Ramazan', 'Ozkan', 'Aynur', 'Azra', 'Sait', 'Mustafa']
    return render_template("deneme.html", isimler=names)


if __name__ == '__main__':
    app.run(debug=True)
