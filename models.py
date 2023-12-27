from flask_login import UserMixin
from . import db

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) # id пользователя
    login = db.Column(db.String(255), unique=True, nullable=True) # login пользователя
    password = db.Column(db.String(1000), nullable=True) # хэш от пароля пользователя
    name = db.Column(db.String(120), nullable=True) # имя пользователя
    icon = db.Column(db.String(255)) # картинка в профиле пользователя

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(2000))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
