from flask import render_template, request, redirect, url_for, abort,flash
from . import main
from ..models import User,Pitch,Comment,Upvote,Downvote
from flask_login import login_required, current_user
from .. import db,photos
from .forms import AddComment,Add_Pitch,UpdateProfile

@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''
  interviewpitches = Pitch.query.filter_by(category="Interview-Pitch").order_by(Pitch.posted.desc()).all()
  entertainmentpitches = Pitch.query.filter_by(category="Entertainment-Pitch").order_by(Pitch.posted.desc()).all()
  investorpitches = Pitch.query.filter_by(category="Investor-Pitch").order_by(Pitch.posted.desc()).all()
  lovepitches = Pitch.query.filter_by(category="Love-Pitch").order_by(Pitch.posted.desc()).all()
  promotionpitches = Pitch.query.filter_by(category="Promotion-Pitch").order_by(Pitch.posted.desc()).all()

  pitches = Pitch.query.filter_by().first()
  like = Upvote.get_by_pitch(pitch_id=Pitch.id)
  dislike = Downvote.get_by_pitch(pitch_id=Pitch.id)

  title = "pitching app"
  return render_template('index.html', title = title, pitches = pitches, interviewpitches = interviewpitches, investorpitches = investorpitches, lovepitches = lovepitches, promotionpitches = promotionpitches,entertainmentpitches=entertainmentpitches)


@main.route('/all_pitches/<id>')
def all_pitches():
  pitches = Pitch.query.all()
  comments = Comment.query.all()
  title = "All Pitches"
  return render_template("allpitches.html", pitches=pitches, comments=comments, title=title)

@main.route('/user_pitch/<users_id>')
def pitch_by_user(users_id):
  pitches = Pitch.get_users_pitch(users_id)
  user = User.query.filter_by(id=users_id).first()
  title = f"{current_user.username}'s Pitches"
  return render_template("profile.html",pitches=pitches,title=title)

@main.route('/new_pitch',methods=["GET","POST"])
@login_required
def new_pitch():
  form = Add_Pitch()
  if form.validate_on_submit():
    title = form.title.data
    pitch_content = form.pitch_content.data
    user = current_user
    category = form.category.data
    pitch = Pitch(pitch_content=pitch_content, title=title, user_id=current_user._get_current_object().id,category=category)
    pitch.save_pitch()

    flash("Pitch successfully posted")
    return redirect(url_for('main.index'))

  title="New Pitch"
  return render_template('pitch.html', title = title, form = form)

@main.route("/user<uname>")
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    title = current_user.username + " | Pitch"
    if user is None:
        abort(404)
    # pitches = Pitch.get_users_pitch(User.id).all()
    # comments=Comment.query.filter_by(user_id=User.id).all()
    # upvotes=Upvote.query.filter_by(user_id=User.id).all()
    # downvotes=Downvote.query.filter_by(user_id=User.id).all()
    return render_template("profile/profile.html", user=user, title=title)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)

@main.route("/user/<uname>/update/pic",methods=["POST"])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
  return redirect(url_for('main.profile',uname=uname))


@main.route('/comment/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def comment(pitch_id):
    form = AddComment()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id=pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment=comment, user_id=user_id, pitch_id=pitch_id)
        new_comment.save_comment()
        return redirect(url_for('.comment',pitch_id=pitch_id))
    return render_template('comment.html', form=form, pitch=pitch, all_comments=all_comments)


@main.route('/like/<int:id>', methods=['GET', 'POST'])
@login_required
def like(id):
    get_pitches = Upvote.get_by_pitch(id)
    get_user = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        upvotes = f'{pitch}'
        if get_user == upvotes:
            return redirect(url_for('main.index', id=id))
        else:
            continue
    new_vote = Upvote(user=current_user, pitch_id=id)
    new_vote.save_upvotes()
    return redirect(url_for('main.index', id=id))


@main.route('/dislike/<int:id>', methods=['GET', 'POST'])
@login_required
def dislike(id):
    get_pitch = Downvote.get_by_pitch(id)
    get_user = f'{current_user.id}:{id}'
    for pitch in get_pitch:
        downvotes = f'{pitch}'
        if get_user == downvotes:
            return redirect(url_for('main.index', id=id))
        else:
            continue
    new_downvote = Downvote(user=current_user, pitch_id=id)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index', id=id))