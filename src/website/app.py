from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Thomas!</p>"


def main():
    app.run(host='0.0.0.0', debug=True)

if __name__ == "__main__":
    main()
