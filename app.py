from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def hello():
    return 'hello world~'


if __name__ == "__main__":
    app.run()
