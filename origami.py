from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<p>Hello World!</p>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"
if __name__ == '__main__':
    Flask.app(Debug=True)