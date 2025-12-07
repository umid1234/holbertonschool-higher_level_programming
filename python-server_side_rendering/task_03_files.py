#!/usr/bin/python3
"""
Flask application that reads products from JSON or CSV files
based on query parameters and displays them using Jinja templates.
"""

from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


def load_json_products():
    """Reads products from products.json"""
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except Exception:
        return None


def load_csv_products():
    """Reads products from products.csv"""
    products = []
    try:
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric fields
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except Exception:
        return None


@app.route("/products")
def products():
    """Display products based on source (json/csv) and optional id filter."""
    source = request.args.get("source")
    prod_id = request.args.get("id", None)

    error_message = None
    data = None

    # ---- Validate source parameter ----
    if source == "json":
        data = load_json_products()
    elif source == "csv":
        data = load_csv_products()
    else:
        error_message = "Wrong source"
        return render_template("product_display.html",
                               error=error_message, products=None)

    # If file couldn't be read
    if data is None:
        error_message = "Error reading file"
        return render_template("product_display.html",
                               error=error_message, products=None)

    # ---- Optional ID filtering ----
    if prod_id is not None:
        try:
            prod_id = int(prod_id)
        except ValueError:
            return render_template("product_display.html",
                                   error="Invalid ID", products=None)

        filtered = [p for p in data if p.get("id") == prod_id]

        if not filtered:
            return render_template("product_display.html",
                                   error="Product not found", products=None)

        # Show only the product with matching ID
        data = filtered

    # ---- Render template with product list ----
    return render_template("product_display.html", products=data, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
