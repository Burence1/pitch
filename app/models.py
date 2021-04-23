from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class User(UserMixin,db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(255),index = True)
  email = db.Column(db.String(255),unique = True)
  bio = db.Column(db.String(255))
  password_hash = db.Column(db.String(255))
  profile_path = db.Column(db.String(255))
  pitches = db.relationship('Pitch',backref='user',lazy="dynamic")

class Pitch(db.Model):
  __tablename__ = 'pitches'

  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(255))
  category = db.Column(db.String(255))
  posted = db.Column(db.DateTime,default=datetime.utcnow)
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))