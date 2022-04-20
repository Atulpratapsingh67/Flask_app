from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired

# Form for login
class loginForm(FlaskForm):
    email = EmailField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])

    submit = SubmitField("Login",validators=[DataRequired()])