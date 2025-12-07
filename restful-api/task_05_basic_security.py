#!/usr/bin/python3
"""
API Security and Authentication Exercise:
- Basic Auth using Flask-HTTPAuth
- JWT Authentication using Flask-JWT-Extended
- Role-based access control
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# ---- JWT Setup ----
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"
jwt = JWTManager(app)

# ---- In-Memory User Store ----
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ==========================
# BASIC AUTHENTICATION
# ==========================

@auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth username + password"""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ==========================
# JWT AUTHENTICATION
# ==========================

@app.route("/login", methods=["POST"])
def login():
    """
    Authenticates user and returns a JWT token.
    Expected JSON: { "username": "...", "password": "..." }
    """
    try:
        data = request.get_json()
        if data is None:
            raise ValueError
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT token with user identity + role
    token = create_access_token(
        identity={"username": username, "role": users[username]["role"]}
    )

    return jsonify({"access_token": token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# ==========================
# ROLE-BASED ACCESS CONTROL
# ==========================

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()

    if identity.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ==========================
# REQUIRED JWT ERROR HANDLERS (All return 401)
# ==========================

@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
