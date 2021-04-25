from wtforms import SubmitField,StringField,TextAreaField,SelectField
from flask_wtf import FlaskForm
from wtforms.validators import Required
from ..models import User, Pitch, Comment, Upvote, Downvote
from flask_login import login_required, current_user


class Add_Pitch(FlaskForm):
  title = StringField('Pitch Title',validators=[Required()])
  category = SelectField('Category', choices=[('Interview-Pitch','Interview Pitch'),('Entertainment-Pitch','Entertainment Pitch'),('Investor-Pitch','Investor Pitch'),('Love-Pitch','Love Pitch'),('Promotion-Pitch','Promotion Pitch')], validators=[Required()])
  pitch_content = TextAreaField("Input pitch",validators=[Required()])
  submit = SubmitField("Submit")

class UpdateProfile(FlaskForm):
  bio = TextAreaField("Enter bio.", validators=[Required()])
  submit = SubmitField("Submit")
  

class AddComment(FlaskForm):
    comment = TextAreaField('Leave a comment', validators=[Required()])
    submit = SubmitField('Submit')