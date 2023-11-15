from flask import Flask

my_app=Flask(__name__)
@my_app.route('/')
def index():
    return 'Hello, Flask App!'
@my_app.route('/logout')
def logout():
    return 'Logged out successfully.'
if __name__=='__main__':
    my_app.run(debug=True)

from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app=Flask(__name__)
app.secret_key="supersecretkey"

blueprint=make_google_blueprint(
    client_id="",
    client_secret="",
    scope=["profile", "email"],
    redirect_to="google_login",
    redirect_url="/login/google"
)
app.register_blueprint(blueprint, url_prefix="/login")
@my_app.route("/")
def index():
    return redirect(url_for("google.login"))
if __name__=="__main__":
    app.run(debug=True)