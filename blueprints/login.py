from flask import render_template, flash, redirect, url_for,Blueprint
from flask_login import login_user, logout_user, login_required
from forms.loginForm import loginForm
from werkzeug.security import check_password_hash
from Models.userModel import Users
from db import db

# Making a bLueprint for Logging screen
loggedin = Blueprint('loggedin',__name__,template_folder="templates")

# Login route
@loggedin.route('/',methods=['GET', 'POST'])
def login():
    try:
        form = loginForm()
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user:
                if check_password_hash(user.password,form.password.data):
                    login_user(user)
                    if user.role == 'EMP':
                        return redirect(url_for('employee.emplogin'))
                    else:
                        return redirect(url_for('admin.dashboard'))
                else:
                    flash("Wrong Password - Try Again!")
            else:
                flash("That User Doesn't Exist! Try Again...")
        return render_template('login.html',form=form)
    except:
        db.create_all()
        flash("That User Doesn't Exist! Try Again...")
        return redirect('/')

# Logout route
@loggedin.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    try:
        logout_user()
        flash("You Have Been Logged Out!  Thanks For Stopping By...")
        return redirect(url_for('loggedin.login'))
    except:
        flash("You Have Been Logged Out!  Thanks For Stopping By...")
        return redirect(url_for('loggedin.login'))
