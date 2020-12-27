# Hello world app 

from flask import Flask

app = Flask(__name__)  # object is being defined


@app.route("/")
def head():
    return "Hello World!"


@app.route("/second")
def second():
    return "This is the second page"


@app.route("/third/subthird")
def third():
    return "This is the subthird of third"


@app.route("/forth/<string:id>")
def forth(id):
    return f"Id of this page is {id}"


if __name__ == "__main__":  # testing and telling our mistakes.
    app.run(debug=True)  # at local
    # app.run(host="0.0.0.0", port=80) #  at ec2
