from flask import (
  Flask,
  render_template,
  request,
  redirect,
  url_for,
  flash,
  make_response,
  session
)
from logging import getLogger as Logger


app = Flask(__name__)
logger = Logger(__name__)


@app.get('/')
def home():
	context = {'title': 'Home'}
	return render_template('home.html', **context)


@app.get('/login')
def login_new():
  context = {'title': 'Login'}
  return render_template('login.html', **context)


@app.post('/login')
def login_create():
  if request.form.get('full_name') != '' and request.form.get('e_mail') != '':
    response = make_response(redirect(url_for('account')))
    response.set_cookie('full_name', request.form.get('full_name'))

    session['e_mail'] = request.form.get('e_mail')
    flash('Welcome!', 'success')

    return response
  else:
    context = {
      'title': 'Login',
      'full_name': request.form.get('full_name'),
      'e_mail': request.form.get('e_mail')
    }
    flash('Full name or e-Mail are blank!', 'error')
    return render_template('login.html', **context)


@app.get('/account')
def account():
  context = {
    'title': request.cookies.get('full_name'),
    'full_name': request.cookies.get('full_name')
  }
  return render_template('account.html', **context)


@app.get('/logout')
def logout():
  session.pop('e_mail', None)

  flash('See you later!', 'success')
  return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(e):
  logger.warning(e)

  context = {
    'title': 'Page not found =(',
    'url': request.referrer,
  }
  return render_template('404.html', **context), 404
