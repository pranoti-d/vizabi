from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_babel import _, lazy_gettext as _l


class SearchForm(FlaskForm):
    seachString = StringField('search')
    q = StringField(_l('search'))
    submit = SubmitField('submit')
    
    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)

class resultForm(FlaskForm):
    textvalue = StringField('Hello World')
    
