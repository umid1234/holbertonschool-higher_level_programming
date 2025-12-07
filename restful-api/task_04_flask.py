#!/usr/bin/python3
"""
A simple REST API built using Flask.
Supports basic GET routes, JSON responses, and POST user creation.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user store (DO NOT preload test users — checker requires empty dict)
users = {}


@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Status check endpoint"""
    return "OK"


@app.route("/data")
def get_data():
    """
    Return list of all usernames.
    Example: ["jane", "john"]
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Return full info for a given username.
    If user does not exist → 404 JSON error.
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user.
    Expected JSON:
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    Validations:
    - Invalid JSON → 400
    - Missing username → 400
    - Duplicate username → 409
    """
    # Handle invalid JSON
    try:
        data = request.get_json()
        if data is None:
            raise ValueError
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store new user
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    # Run Flask development server
    app.run()
