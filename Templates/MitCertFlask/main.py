#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, flash
from flask_login import LoginManager
from flask_wtf import FlaskForm, CsrfProtect
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from config import Config
from controllers import MitigatingCircumstanceController

from google.appengine.ext import ndb
from google.appengine.api import users

app = Flask(__name__)
CsrfProtect(app)
app.config.from_object(Config)

class ExampleForm(FlaskForm): #Flask forms are created as a class and called into a page 
    name = StringField('InputName:', validators=[DataRequired()])
    email = StringField('InputEmail:', validators=[DataRequired()])
    reason = StringField('InputReason:', validators=[DataRequired()])
    submit = SubmitField('')


@app.route('/')
def hello_world():
    user = users.get_current_user()
    if user:
        nickname = user.nickname()
        logout_url = users.create_logout_url('/')
        greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
            nickname, logout_url)
    else:
        login_url = users.create_login_url('/')
        greeting = '<a href="{}">Sign in</a>'.format(login_url)
    return render_template("index.html")




@app.route('/exampleform', methods=['GET','POST'])
def login():
    form = ExampleForm(request.form) #allows for the class to get data from the form 

    if form.validate_on_submit(): # checks that all fields have data
        ## put database crud stuff here

        MitigatingCircumstanceController().create(
            name = request.form['name'],
            email = request.form['email'],
            reason = request.form['reason']
        )

        print request.form['name']
        print request.form['email']
        print request.form['reason']
       
        flash('name: {}, email: {}, reason: {}'.format(
                form.name.data, form.email.data, form.reason.data))
        return redirect('/index')
  


    return render_template('form.html', title='ExampleForm', form=form)
