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

@bp.route('/search')
def search():
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(g.search_form.q.data, page,
                               current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title=_('Search'), posts=posts,
                           next_url=next_url, prev_url=prev_url)
