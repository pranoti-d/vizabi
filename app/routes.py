from app import app
from flask import render_template
#from app import server
from flask import g
from app import models

def before_request():
    g.search_form = SearchForm()
    g.locale = str(get_locale())

@app.route('/')
@app.route('/index')
def index():
    return render_template('index_1.html', title='Home')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template('index_1.html', title='Home')

@app.route('/search')
def search():
    form = SearchForm()
    return render_template('search.html', title='Search', form=form)
