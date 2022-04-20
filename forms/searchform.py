from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import DataRequired

# Form for search
class SearchForm(FlaskForm):
    email = EmailField("Email",validators=[DataRequired()])

    submit = SubmitField("Search",validators=[DataRequired()])
