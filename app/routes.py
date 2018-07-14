from app import app
from flask import render_template
#from app import server
from flask import g
from app.forms import SearchForm

@bp.before_app_request
def before_request():
    g.search_form = SearchForm()
    g.locale = str(get_locale())

@app.route('/')
@app.route('/index')
def index():
    return render_template('index_1.html', title='Home')
