from flask_sqlalchemy import SQLAlchemy
from bcrypt import gensalt, hashpw


db = SQLAlchemy()


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(32), nullable=False)
  surname = db.Column(db.String(32), nullable=False)
  e_mail = db.Column(db.String(64), nullable=False, unique=True)
  passhash = db.Column(db.String(128), nullable=False)


  @property
  def password(self):
    raise AttributeError('password not readable')


  @password.setter
  def password(self, password):
    self.passhash = hashpw(password.encode('utf-8'), gensalt())


  def __repr__(self):
    return f'User("{self.name}", "{self.surname}", "{self.e_mail}")'
