from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User,Pitch,Comment,Upvote,Downvote
from flask_login import login_required, current_user
from .. import db

@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''

  title = "pitching app"

  if user is None:
    pitches = Pitch.query.all()
    return render_template('index.html',title=title,pitches=pitches)

  if user is not None:
    pitches=Pitch.get_users_pitch(user.id)
    return redirect(url_for('.profile',username=username,pitches=pitches))
