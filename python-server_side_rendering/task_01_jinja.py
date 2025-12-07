#!/usr/bin/python3
"""
Basic Flask application rendering HTML templates with reusable
header and footer components.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render home page"""
    return render_template("index.html")


@app.route("/about")
def about():
    """Render About page"""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Render Contact page"""
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
