from flask import Flask, render_template

AppServer = Flask(__name__)

@AppServer.route('/')
@AppServer.route('/home')
def home():
    return render_template('pages/home.html')
