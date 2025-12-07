from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    """Reads data from the JSON file."""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def read_csv():
    """Reads data from the CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except FileNotFoundError:
        return []
    return products

def read_sql():
    """Reads data from the SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # This allows us to access columns by name (row['name'])
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        
        # Convert SQLite rows to a list of dictionaries
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        conn.close()
    except sqlite3.Error as e:
        return []
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products_list = []
    error_msg = None

    # 1. Fetch data based on source
    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    elif source == 'sql':
        products_list = read_sql()
    else:
        error_msg = "Wrong source"

    # 2. Filter by ID (if no error so far)
    if not error_msg and product_id:
        try:
            p_id = int(product_id)
            # Filter the list (Works for JSON, CSV, and SQL data)
            products_list = [p for p in products_list if p['id'] == p_id]
            
            if not products_list:
                error_msg = "Product not found"
        except ValueError:
            error_msg = "Product not found"

    return render_template('product_display.html', products=products_list, error=error_msg)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
