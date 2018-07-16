from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    seachString = StringField('search')
    submit = SubmitField('submit')
