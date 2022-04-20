from flask import Blueprint
from Models.userModel import Users
from forms.registerForm import registerForm
from flask import flash, render_template, redirect, url_for,session
from db import db
from sqlalchemy import or_
from werkzeug.security import generate_password_hash

# Making a bLueprint for Register
signup = Blueprint('signup',__name__,template_folder="templates")

# Route for register
@signup.route('/register',methods=['GET', 'POST'])
def register():
    
        form = registerForm()
        if form.validate_on_submit():
            if form.password.data == form.confirm.data:
                try:
                    user = Users.query.filter( or_ (Users.email.like(form.email.data), Users.phone.like(form.phone.data)) ).first()
                except:
                    db.create_all()
                    user = None
                if user:
                    flash(message="Email already registered!!!")
                else:
                    user = Users(firstName = form.FirstName.data,
                                lastName = form.LastName.data,
                                email = form.email.data,
                                phone = form.phone.data,
                                dob = form.dob.data,
                                address = form.address.data,
                                password = generate_password_hash(form.password.data))
                    db.session.add(user)
                    db.session.commit()
                    flash(message="Registered successful!!")
                    return redirect(url_for('loggedin.login'))
            else:
                flash(message="Password doesn't match!!")
                return redirect(url_for('register'))
        return render_template('register.html',form=form)
