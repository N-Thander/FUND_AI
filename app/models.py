# app/models.py
from . import db
from sqlalchemy.ext.declarative import declared_attr
import uuid

class UserProfileData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(36), unique=True, nullable=False, default=str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email_id = db.Column(db.String(120), unique=True, nullable=False)
    contact_number = db.Column(db.String(15), nullable=True)
    password = db.Column(db.String(200), nullable=False)

    @staticmethod
    def generate_user_id():
        return str(uuid.uuid4())
