from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

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

  @property
  def password(self):
    raise AttributeError('Cannot read password attribute')

  @password.setter
  def password(self,password):
    self.password_hash = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.password_hash,password)

  def __repr__(self):
    return f'User {self.username}'

class Pitch(db.Model):
  __tablename__ = 'pitches'

  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(255))
  pitch_content = db.column(db.String(255))
  posted = db.Column(db.DateTime,default=datetime.utcnow)
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
  category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
  comments = db.relationship('Comment',backref='pitch',lazy="dynamic")
  upvotes = db.relationship('Upvote',backref='pitch',lazy="dynamic")
  downvotes=db.relationship('Downvote',backref='pitch',lazy="dynamic")

  def save_pitch(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_users_pitch(cls,id):
    user_pitch = Pitch.query.filter_by(user_id=id).order_by(Pitch.posted.desc())
    return user_pitch

  @classmethod
  def get_by_category(cls,id):
    pitch_category=Pitch.query.filter_by(category_id=id).order_by(Pitch.posted.desc())
    return pitch_category

  def __repr__(self):
    return f"Pitch {self.title}"

class Category(db.Model):
  __tablename__="categories"
  id = db.Column(db.Integer,primary_key=True)
  category_title = db.Column(db.String(255))
  pitches = db.relationship('Pitch',backref='category',lazy="dynamic")

  @classmethod
  def get_category(cls,title):
    category_title = Category.query.filter_by(category_title=category_title).first()
    return category_title

  def __repr__(self):
      return f'Category{self.category_title}'

class Comment(db.Model):
  __tablename__='comments'

  id = db.Column(db.Integer,primary_key=True)
  contents = db.Column(db.Integer)
  pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    comments=Comment.query.filter_by(pitch_id=id).all()
    return comments

  def __repr__(self):
    return f'Comment{self.contents}'

class Upvote(db.Model):
  __tablename__='upvotes'

  id=db.Column(db.Integer,primary_key=True)
  counter=db.Column(db.Integer)
  user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
  pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

  def save_upvotes(self):
    db.session.add(self)
    db.session.commit()
  
  @classmethod
  def get_by_pitch(cls,id):
    upvote_by_pitch=Upvote.query.filter_by(pitch_id=id).all()
    return upvote_by_pitch

  def __repr__(self):
    return f'Upvote{self.counter}'

class Downvote(db.Model):
  __tablename__='downvotes'

  id=db.Column(db.Integer,primary_key=True)
  counter = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

  def save_downvotes(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_by_pitch(cls, id):
    downvote_by_pitch = Downvote.query.filter_by(pitch_id=id).all()
    return downvote_by_pitch

  def __repr__(self):
    return f'Downvote{self.counter}'
