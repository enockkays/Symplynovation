from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/profile/<name>")
def profile(name):
    return render_template("Oh My Genes.html", name=name)


if __name__ == '__main__':
    app.run()
