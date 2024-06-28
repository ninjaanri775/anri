from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from ext import db, login_manager


class Shopin(db.Model ):

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String, nullable=False, default="default_photo.jpg")


class User(db.Model, UserMixin ):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String())

    def __init__(self, username, password, role="Guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)