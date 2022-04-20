from db import db
from flask_login import UserMixin

# User model for database to save all information
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(200), nullable=False)
    lastName = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    dob = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(10), nullable=False, default='EMP')
    password = db.Column(db.String(100), nullable=False)    

    def __repr__(self) -> str:
        return 'Email:{0}'.format(self.email)