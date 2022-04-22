# Importing Required Modules
from flask import Flask, render_template
from flask_login import LoginManager
from os import environ
from Models.userModel import Users
from blueprints.register import signup
from blueprints.adminlogin import admin
from blueprints.emplogin import employee
from blueprints.login import loggedin


# Create a flask app
app = Flask(__name__)

# Adding Blueprints
app.register_blueprint(signup, url_prefix="/")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(employee, url_prefix="/")
app.register_blueprint(loggedin, url_prefix="/")



# Add configurations
app.config.from_mapping(
    SECRET_KEY='ATUL',
    SQLALCHEMY_DATABASE_URI='sqlite:///users.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False)

# Login Manage
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))


# Error handling

# # Invalid URL error
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

# Internal server error
@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html')

# App running
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0')