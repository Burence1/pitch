from flask import render_template, request, redirect, url_for, abort,flash
from . import main
from ..models import User,Pitch,Comment,Upvote,Downvote,Category
from flask_login import login_required, current_user
from .. import db
from .forms import Add_Category,Add_Comment,Add_Pitch

@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''

  title = "pitching app"

  categories = Category.query.all()
  return render_template('index.html',title=title,categories=categories)

@main.route('/addcategory',methods=["GET","POST"])
@login_required
def add_category():
  form = Add_Category()
  if current_user.username != 'burens':
    abort(404)

  if form.validate_on_submit():
    category = Category(category_title=form.category_title.data)
    db.session.add(category)
    db.session.commit()
    return redirect(url_for("main.index"))

  title = "New categories"
  return render_template("new_category.html",cat_form=form,title=title)

@main.route('/pitches/<category_id>')
def pitch_by_category(category_id):
  pitches = Pitch.get_by_category(category_id)
  category = Category.query.filter_by(id=category_id).first()
  category_title = category.category_title
  categories = Category.query.all()
  comments = Comment.query.all()
  title = f"{category_title} Pitch"
  return render_template("categories.html",pitches=pitches,category_title=category_title,comments=comments,title=title,categories=categories)

@main.route('/user_pitch/<user_id>')
def pitch_by_user(user_id):
  pitches = Pitch.get_users_pitch(user_id)
  user = User.query.filter_by(id=user_id).first()
  category = Category.query.filter_by(id=user_id).first()
  username = user.username
  comments = comments.query.all()
  title = f"{current_user.username}'s Pitches"
  return render_template("usercategory.html",pitches=pitches,username=username,comments=comments,title=title)

@main.route('/new_pitch',methods=["GET","POST"])
@login_required
def new_pitch():
  form = Add_Pitch()
  categories = Category.query.all()
  if form.validate_on_submit():
    category_id = Category.get_category(form.category.data)
    pitch = Pitch(pitch_content=form.pitch_content.data,author=current_user,title=form.title.data,categories = Category.query.all())
    db.session.add(pitch)
    db.session.commit()

    flash("Pitch successfully posted")
    return redirect(url_for("auth.pitchcategories",category_id=category_id))

  title="New Pitch"
  return render_template("createpitch.html",title=title,pitch_form =form,categories=categories)


@main.route("/new_comment/<int:pitch_id>",methods=["GET","POST"])
@login_required
def new_comment(pitch_id):
  form = Add_Comment()
  categories = Category.query.all()
  pitch = Pitch.query.filter_by(id=pitch_id).first()
  if form.validate_on_submit():
    comment = Comment(contents=form.contents.data,pitch_id=pitch_id,author=current_user)
    db.session.add(comment)
    db.session.commit()

    flash("Your comment has been added")
    return redirect(url_for('auth.pitchcategories',category_id=pitch.category_id))

  return render_template("add_comment.html",comment_form=form,categories=categories,pitch=pitch)