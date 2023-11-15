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