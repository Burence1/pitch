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
  comments = db.relationship('Comment',backref='user',lazy="dynamic")
  upvotes = db.relationship('Upvote', backref='user', lazy="dynamic")
  downvotes = db.relationship('Downvote',backref='user',lazy="dynamic")

class Pitch(db.Model):
  __tablename__ = 'pitches'

  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(255))
  category = db.Column(db.String(255))
  posted = db.Column(db.DateTime,default=datetime.utcnow)
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
  comments = db.relationship('Comment',backref='pitch',lazy="dynamic")
  upvotes = db.relationship('Upvote',backref='pitch',lazy="dynamic")
  downvotes=db.relationship('Downvote',backref='pitch',lazy="dynamic")

class Comment(db.Model):
  __tablename__='comments'

  id = db.Column(db.Integer,primary_key=True)
  contents = db.Column(db.Integer)
  pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Upvote(db.Model):
  __tablename__='upvotes'

  id=db.Column(db.Integer,primary_key=True)
  counter=db.Column(db.Integer)
  user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
  pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))


class Downvote(db.Model):
  __tablename__='downvotes'

  id=db.Column(db.Integer,primary_key=True)
  counter = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))