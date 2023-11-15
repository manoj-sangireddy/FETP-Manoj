from flask import Flask

my_app=Flask(__name__)
@my_app.route('/')
def index():
    return 'Hello, Flask App!'

from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

my_app=Flask(__name__)
my_app.secret_key="supersecretkey"

blueprint=make_google_blueprint(
    client_id="GOOGLE_CLIENT_ID",
    client_secret="GOOGLE_CLIENT_SECRET",
    scope=["profile", "email"],
    redirect_to="google_login",
    redirect_url="https://127.0.0.1:5000/login/google"
)
my_app.register_blueprint(blueprint, url_prefix="/login")

@my_app.route("/")
def index():
    return redirect(url_for("google.login"))


@my_app.route("/login/google")
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp=google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]
    name=resp.json()["name"]
    picture=resp.json()["picture"]
    return f"Hello {name} [<a href='/logout'>Sign out</a>]<br>You are signed in with email {email}<br><img src='{picture}'alt='Profile Picture'>"

@my_app.route('/logout')
def logout():
    return 'Logged out successfully.'

if __name__=="__main__":
    my_app.run(debug=True)
