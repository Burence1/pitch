from flask import render_template,url_for,redirect,flash,request
from . import auth
from flask_login import login_user,logout_user,login_required
from app.models import User
from .. import db