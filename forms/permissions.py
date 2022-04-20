from flask_wtf import FlaskForm
from wtforms import SubmitField,HiddenField,EmailField
from wtforms.validators import DataRequired

# Form for login
class permissionsForm(FlaskForm):
    email = EmailField()
    submit = SubmitField("Give Admin Rights",validators=[DataRequired()])