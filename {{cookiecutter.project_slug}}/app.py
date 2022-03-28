"""Web app for {{ cookiecutter.app_name }}."""
import json
import os
from flask import Flask, request, redirect, send_file
from pathlib import Path
from requests_oauthlib import OAuth2Session


def get_secret(path: Path, env_var: str) -> str:
    """Get secret from a path or an environment variable.

    If built via docker-compose, the secrets will be in file. If heroku
    is used instead, the content will be in an environment variable

    Args:
        path (Path): path object of the file containing the secret
        env_var (str): environment variable with the secret

    Raises:
        KeyError: If the secret is in neither of the arguments

    Returns:
        str: value of the secret
    """
    try:
        return os.environ.get(env_var) or path.read_text()
    except FileNotFoundError:
        raise KeyError(env_var)


CLIENT_ID = get_secret(Path("/run/secrets/client_id"), "OAUTH2_CLIENT_ID")
CLIENT_SECRET = get_secret(Path("/run/secrets/client_secret"), "OAUTH2_CLIENT_SECRET")
SCOPES = get_secret(Path("/run/secrets/scopes"), "OAUTH2_REQUESTED_SCOPES").split()
FLASK_SECRET_KEY = get_secret(Path("/run/secrets/flask_secret"), "FLASK_SECRET_KEY")


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
MARKETPLACE_HOST = os.environ["MARKETPLACE_HOST"]
CALLBACK_URL = os.environ["CALLBACK_URL"]

AUTH_URL = f"{MARKETPLACE_HOST}/auth/realms/marketplace/protocol/openid-connect/auth"
TOKEN_URL = f"{MARKETPLACE_HOST}/auth/realms/marketplace/protocol/openid-connect/token"
USER_INFO = (
    f"{MARKETPLACE_HOST}/auth/realms/marketplace/protocol/openid-connect/userinfo"
)


app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY


@app.route("/")
def index():
    doc = """
        <html>
            <h1> {{ cookiecutter.app_name }} </h1>
            <p><a href=login>Log in</a></p>
        </html>
    """
    return doc


@app.route("/app/image")
def logo():
    return send_file("static/images/logo.png", mimetype="image/png")


@app.route("/headers")
def headers():
    return json.dumps(dict(request.headers))


@app.route("/login")
def login():
    oauth_session = OAuth2Session(CLIENT_ID, redirect_uri=CALLBACK_URL, scope=SCOPES)
    authorization_url, _ = oauth_session.authorization_url(AUTH_URL)
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    scope_request = request.args.get("scope")
    oauth_session = OAuth2Session(
        CLIENT_ID, redirect_uri=CALLBACK_URL, scope=scope_request
    )
    try:
        oauth_session.fetch_token(
            TOKEN_URL,
            client_secret=CLIENT_SECRET,
            authorization_response=request.url,
            scope=scope_request,
            verify=False,
        )
    except Exception:
        return request.args.get("error_description")
    user = oauth_session.get(USER_INFO)

    return user.content


@app.route("/heartbeat")
def heartbeat():
    return "{{ cookiecutter.app_name }} : application running."
