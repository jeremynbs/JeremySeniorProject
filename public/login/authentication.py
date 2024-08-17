import sqlite3
from flask import Flask, redirect, url_for, request
from flask_dance.contrib.google import make_google_blueprint, google

# Create Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"

# Configure Google OAuth
app.config["GOOGLE_OAUTH_CLIENT_ID"] = "your_client_id"
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = "your_client_secret"
google_bp = make_google_blueprint(scope=["profile", "email"])
app.register_blueprint(google_bp, url_prefix="/login")

# Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        name TEXT NOT NULL,
        picture TEXT NOT NULL,
        jwt TEXT NOT NULL
    )
""")
conn.commit()

# Gateway route
@app.route("/")
def gateway():
    if not google.authorized:
        return redirect(url_for("google.login"))
    
    resp = google.get("/oauth2/v2/userinfo")
    email = resp.json()["email"]
    
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    
    if user:
        return redirect(url_for("login"))
    else:
        return redirect(url_for("register"))

# Register route
@app.route("/register")
def register():
    if not google.authorized:
        return redirect(url_for("google.login"))
    
    resp = google.get("/oauth2/v2/userinfo")
    email = resp.json()["email"]
    name = resp.json()["name"]
    picture = resp.json()["picture"]
    jwt = google.token["access_token"]
    
    cursor.execute("INSERT INTO users (email, name, picture, jwt) VALUES (?, ?, ?, ?)", (email, name, picture, jwt))
    conn.commit()
    
    return "Registration successful!"

# Login route
@app.route("/login")
def login():
    email = request.args.get("email")
    
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    
    if user:
        return f"Welcome back, {user[2]}!"
    else:
        return "User not found."

if __name__ == "__main__":
    app.run()