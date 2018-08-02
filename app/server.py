from flask import Flask, render_template

AppServer = Flask(__name__)

@AppServer.route('/')
@AppServer.route('/index')
def home():
    return render_template('home.html')
