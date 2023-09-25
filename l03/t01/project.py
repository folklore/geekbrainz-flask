from flask import Flask, render_template, request, make_response, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from models import db, User
from logging import getLogger as Logger
from registration_form import RegistrationForm


app = Flask(__name__)
logger = Logger(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
db.init_app(app)
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
  db.create_all()
  print('OK')


@app.get('/')
def home():
  context = {'title': 'Home', 'users': User.query.all()}
  return render_template('home.html', **context)


@app.get('/sign_up/')
def sign_up_new():
  form = RegistrationForm()
  return render_template('sign_up.html', form=form)


@app.post('/sign_up/')
def sign_up_create():
  form = RegistrationForm()

  if form.validate():
    user = User(
      name=form.name.data,
      surname=form.surname.data,
      e_mail=form.e_mail.data,
      password=form.password.data
    )
    db.session.add(user)
    db.session.commit()

    response = make_response(redirect(url_for('home')))
    flash('SignUp was successfully!', 'success')
    return response
  else:
    return render_template('sign_up.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
  logger.warning(e)

  context = {
    'title': 'Page not found =(',
    'url': request.referrer,
  }
  return render_template('404.html', **context), 404
