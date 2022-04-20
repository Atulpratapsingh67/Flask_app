from flask import Blueprint
from flask import render_template
from flask_login import current_user

# Making a bLueprint for employee login
employee = Blueprint('employee',__name__,template_folder="templates")

# Adding route for employee details
@employee.route('/employee',methods=['GET','POST'])
def emplogin():
    return render_template('emplogin.html' , user = current_user)