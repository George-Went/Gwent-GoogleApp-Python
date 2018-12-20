#!/usr/bin/env python
from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from google.appengine.ext import ndb


login_manager = LoginManager()

class MitigatingCircumstance(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty() 
    issue = ndb.StringProperty()
    comment = ndb.StringProperty()

#class MitigatingCircumstance(Form)

#name of the application that uses the flask framework
app = Flask(__name__)
login_manager.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/salvador")
def salvador():
    return render_template("salvador.html")

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submitted_form', methods=['POST'])
def submitted_form():
    name = request.form['name']
    phone = request.form['phone']
    issue = request.form['issue']
    comment = request.form['comment']

    submission = name + 'MitigatingCirtumstance' 

    submission = MitigatingCircumstance(name = request.form['name'],
                                    phone = request.form['phone'],
                                    issue = request.form['issue'],
                                    comment = request.form['comment'])
    
    submission.put()


    return render_template(
    'submitted_form.html',
    name=name,
    phone=phone,
    issue=issue,
    comment=comment)


# Our mock database.
users = {'foo@bar.tld': {'password': 'secret'}}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user



@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'