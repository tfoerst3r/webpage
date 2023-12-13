from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


def main():
    app.run(host='0.0.0.0', debug=True)

if __name__ == "__main__":
    main()
