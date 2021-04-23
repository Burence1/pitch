from flask import render_template,url_for,redirect,flash,request
from . import auth
from flask_login import login_user,logout_user,login_required
from app.models import User
from .. import db
from .forms import RegistrationForm,LoginForm

@auth.route('/register',methods=["GET","POST"])
def register():
  form=RegistrationForm
  if form.validate_on_submit():
    user=User(email=form.email.data,username=form.username.data,password=form.password.data)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('auth.login'))

  return render_template('auth/register.html',registration_form=form)

@auth.route('/login',methods=["GET","POST"])
def login():
  login_form=LoginForm
  if form.validate_on_submit():
    user=User.query.filter_by(email=login_form.email.data).first()
    