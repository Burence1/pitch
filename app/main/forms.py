from wtforms import SubmitField,StringField,TextAreaField,SelectField
from flask_wtf import FlaskForm
from wtforms.validators import Required

class Add_Category(FlaskForm):
  category_title=TextAreaField('Add a category',validators=[Required()])
  submit = SubmitField('Submit')

class Add_Comment(FlaskForm):
  contents = TextAreaField('Add comment',validators=[Required()])
  submit = SubmitField('Submit')

class Add_Pitch(FlaskForm):
  title = StringField('Pitch Title',validators=[Required()])
  category = SelectField('Select category',choices=[("Interview","Interview Pitches"),("Product","Product Pitch"),("Love","Love Pitch"),("Investor","Investor Pitches")],validators=[Required()])
  pitch_content = TextAreaField("Input pitch",validators=[Required()])
  submit = SubmitField("Submit")