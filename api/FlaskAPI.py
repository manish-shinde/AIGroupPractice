from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/rakesh")
def salvador():
    return "Hello, Rakesh"


if __name__ == "__main__":
    app.run(debug=True)

# http://127.0.0.1:5000/ plz check in chrome(local api)
