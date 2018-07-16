from app import app
from flask import render_template, flash, redirect, url_for
#from app import server
from flask import g
from app import models
from app.forms import SearchForm, resultForm

def before_request():
    g.search_form = SearchForm()
    g.locale = str(get_locale())

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        # ...
        return redirect('/result')
    return render_template('search.html', title='Search', form=form)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template('index_1.html', title='Home')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    return render_template('search.html', title='Search', form=form)

@app.route('/result', methods=['GET', 'POST'])
def result():
    form = resultForm()
    return render_template('result.html', title='Result', form=form)
