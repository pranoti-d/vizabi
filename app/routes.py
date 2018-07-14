from app import app
from flask import render_template
#from app import server
from flask import g
from app.forms import SearchForm
from app import models

def before_request():
    g.search_form = SearchForm()
    g.locale = str(get_locale())

@app.route('/')
@app.route('/index')
def index():
    return render_template('index_1.html', title='Home')

@app.route('/login', from app import app)
def login():
    return render_template('index_1.html', title='Home')

@app.route('/search', methods = ['POST', 'GET'])
def search():
    list = test_data_dummy_data.query.whoosh_search(request.args.get('nm')).all
    return render_template('search.html', title=_('Search'), posts=list)
