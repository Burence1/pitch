from .. import User
from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Required,EqualTo,Email


class RegistrationForm(FlaskForm):
  email = StringField('Enter your email',validators=[Required(),Email()])
  username = StringField('Enter username',validators=[Required()])
  password = PasswordField('Password',validators=[Required(),EqualTo('password_confrim',
  message='Passwords must match')])
  password_confrim=PasswordField('Confirm Passwords',validators=[Required()])
  submit = SubmitField("Sign Up")

  def validate_user_email(self,data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError("This email has been registered")

  def validate_username(self,data_field):
    if User.query.filter_by(username=data_field.data).first():
      raise ValidationError("Username already in use")

class LoginForm(FlaskForm):
  email=StringField("Enter your email",validators=[Required(),Email()])
  password=PasswordField("Password",validators=[Required()])
  remember=BooleanField("Stay Logged in")
  submit=SubmitField("Log In")