from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
  name = StringField(
    'Name',
    validators=[DataRequired()]
  )

  surname = StringField(
    'Surname',
    validators=[DataRequired()]
  )

  e_mail = StringField(
    'e-Mail',
    validators=[DataRequired(), Email()]
  )

  password = PasswordField(
    'Password',
    validators=[DataRequired()]
  )

  confirmation_password = PasswordField(
    'Password again',
    validators=[DataRequired(), EqualTo('password')]
  )
