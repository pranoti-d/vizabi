from flask import Flask, render_template

AppServer = Flask(__name__)

@AppServer.route('/', methods=['GET', 'POST'])
@AppServer.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('visualization.html')
