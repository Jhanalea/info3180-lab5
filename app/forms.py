from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired



class MovieForm(FlaskForm):
  title = StringField('Movie Title', validators=[InputRequired()])
  description = TextAreaField('Description', validators=[InputRequired()])
  poster = FileField('Movie Poster', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images Only.')])
