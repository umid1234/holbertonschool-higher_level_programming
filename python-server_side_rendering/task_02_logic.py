#!/usr/bin/python3
"""
Flask application to display dynamic content using loops
and conditional statements from a JSON file.
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route("/items")
def items():
    """Reads items from items.json and renders them in a template."""

    json_path = os.path.join(os.path.dirname(__file__), "items.json")

    try:
        with open(json_path, "r") as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except Exception:
        items_list = []  # fallback to empty list

    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
