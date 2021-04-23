from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User,Pitch,Comment,Upvote,Downvote,Category
from flask_login import login_required, current_user
from .. import db
from .forms import Add_Category,Add_Comment,PitchCategory

@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''

  title = "pitching app"

  categories = Category.query.all()
  return render_template('index.html',title=title,categories=categories)

@main.route('/addcategory',methods=["GET","POST"])
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
  