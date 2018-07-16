from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    seachString = StringField('search', validators=[DataRequired()])
    submit = SubmitField('submit')
