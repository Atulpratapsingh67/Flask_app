from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, DateField, PasswordField
from wtforms.validators import DataRequired, length

# Form for register
class registerForm(FlaskForm):
    FirstName = StringField("First Name",validators=[DataRequired()])
    LastName = StringField("Last Name",validators=[DataRequired()])
    email = EmailField("Email",validators=[DataRequired()])
    phone = StringField("Phone Number",validators=[DataRequired(), length(min=10,max=10)])
    dob = DateField("Date of Birth",validators=[DataRequired()])
    address = StringField("Address",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired(), length(min=6)])
    confirm  = PasswordField("Confirm Password",validators=[DataRequired(), length(min=6)])

    submit = SubmitField("Register",validators=[DataRequired()])
