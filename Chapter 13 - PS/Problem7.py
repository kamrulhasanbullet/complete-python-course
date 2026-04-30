# Explore the ‘Flask’ module and create a web server using Flask & Python.

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello, World!</h1><p>Welcome to my first Flask Web Server</p>"


@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This is a simple Flask application.</p>"


if __name__ == "__main__":
    app.run(debug=True)
