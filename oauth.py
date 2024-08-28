import os
import pathlib

import requests
from flask import Flask, session, abort, redirect, request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from dotenv import load_dotenv, dotenv_values
import sqlite3

load_dotenv()

# print(os.getenv("GOOGLE_CLIENT_ID"))


app = Flask("Google Login App")
app.secret_key = os.getenv("GOOGLE_CLIENT_SECRET") # make sure this matches with that's in client_secret.json

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # to allow Http traffic for local dev

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    print(id_info)

    # Connect to the database

    conn = sqlite3.connect('schema/database.db')
    cursor = conn.cursor()

    # Store the required information from id_info
    email = id_info.get("email")
    firstName = id_info.get("given_name")
    lastName = id_info.get("family_name")
    profilePicLink = id_info.get("picture")

    # Store the whole id_info variable
    id_info_data = id_info

    # Check if the user already exists in the database
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        # Merge the data with the existing user
        cursor.execute("UPDATE users SET firstName=?, lastName=?, profilePicLink=?, completeGoogleJWT=? WHERE email=?",
                       (firstName, lastName, profilePicLink, str(id_info_data), email))
    else:
        # Add the new user to the database
        cursor.execute("INSERT INTO users (email, firstName, lastName, profilePicLink, completeGoogleJWT, isAdmin) VALUES (?, ?, ?, ?, ?, ?)",
                       (email, firstName, lastName, profilePicLink, str(id_info_data), 0))

    conn.commit()

    # Close the connection
    conn.close()

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/")
def index():
    return "Hello World <a href='/login'><button>Login</button></a>"


@app.route("/protected_area")
@login_is_required
def protected_area():
    return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
