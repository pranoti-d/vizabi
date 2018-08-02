from flask import Flask
from datetime import datetime
from flask import render_template, redirect

webServer = Flask(__name__)

@webServer.route('/contact')
def contact():
    return render_template('pages/visualization.html')
