from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

# Hardcoded secret (bad!)
API_KEY = "supersecret123"

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    # SQL injection risk
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    return "Logged in!" if user else "Failed!"

@app.route("/hash")
def weak_hash():
    data = request.args.get("data")
    # Weak MD5 hash
    return hashlib.md5(data.encode()).hexdigest()

if __name__ == "__main__":
    app.run(debug=True)  # Debug mode enabled (bad!)
