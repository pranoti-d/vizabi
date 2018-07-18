from app import app
from flask import render_template, flash, redirect, url_for, request, g, current_app
#from app import server
from flask import g
from flask_babel import _, get_locale
from app.models import test_data_dummy_data
from app.forms import SearchForm, resultForm

@app.before_request
def before_request():
    g.search_form = SearchForm()
    #g.locale = str(get_locale())

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    g.search_form = SearchForm()
    #g.locale = str(get_locale())
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
    page = request.args.get('page', 1, type=int)
    lists, total = test_data_dummy_data.search(g.search_form.seachString.data, page,
                               20)
    next_url = url_for('result', q=g.search_form.seachString.data, page=page + 1) \
        if total > page * 20 else None
    prev_url = url_for('result', q=g.search_form.seachString.data, page=page - 1) \
        if page > 1 else None
    return render_template('result.html', title=_('results'), lists=lists,
                           next_url=next_url, prev_url=prev_url, form=form)
    
