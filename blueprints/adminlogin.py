from flask import Blueprint, session
from Models.userModel import Users
from flask import flash, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.searchform import SearchForm
from forms.permissions import permissionsForm
from db import db

# Making a bLueprint for admin
admin = Blueprint('admin',__name__,template_folder="templates")

# Dashboard for admin
@admin.route('/dashboard',methods=['GET', 'POST'])
@login_required
def dashboard():
    # Checking if the current is admin or not
    try:
        if current_user.role == 'ADM':
            return render_template('dashboard.html')
        else:
            flash("Permission Denied")
            return redirect(url_for('loggedin.logout'))
    except:
        flash("Permission Denied")
        return redirect(url_for('loggedin.logout'))
# List of all employees
@admin.route('/dashboard/employees',methods=['GET', 'POST'])
@login_required
def employees():
    # Checking if the current is admin or not
    if current_user.role == 'ADM':
        users = Users.query.all()
        return render_template('employees.html' ,users=users)
    else:
        flash("Permission Denied")
        return redirect(url_for('loggedin.logout'))
    
# Employee details
@admin.route('/dashboard/employeeDetail',methods=['GET', 'POST'])
@login_required
def employeeDetail():
    # Checking if the current is admin or not
    if current_user.role == 'ADM':
        form = SearchForm()
        user =None
        if form.validate_on_submit():
            user = Users.query.filter_by(email = form.email.data).first()
            if user is None:
                flash("Email not registered!!")
        return render_template('employeeDetail.html', form = form, user = user)
    else:
        flash("Permission Denied")
        return redirect(url_for('loggedin.logout'))

# Change permissions
@admin.route('/dashboard/givepermissions',methods=['GET', 'POST'])
@login_required
def givepermissions():
    # Checking if the current is admin or not
    if current_user.role == 'ADM':
        users = Users.query.all()
        form = permissionsForm()
        if form.validate_on_submit():
            user = Users.query.filter_by(email = form.email.data).first()
            user.role = "ADM"
            db.session.commit()
            
        return render_template('permissions.html' ,users=users ,form = form)
    else:
        flash("Permission Denied")
        return redirect(url_for('loggedin.logout'))