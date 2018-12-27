#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_wtf import FlaskForm, CSRFProtect
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.contrib.google import make_google_blueprint, google 

from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from google.appengine.ext import ndb

from forms import LoginForm, ExampleDataForm
from config import Config
#from models import User
from controllers import UserController, ExampleDataController 





app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager()
login_manager.init_app(app)


app.config['SECRET_KEY'] = 'you-will-never-guess'
csrf = CSRFProtect(app)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "your now logged out!"

@app.route('/home')
@login_required
def home():
    return "current user is " + current_user.user_email


@app.route('/')
def login():
    return render_template('/dashboard.html')

@app.route('/dashboard')
def index():
    return render_template('/dashboard.html')

@app.route('/mitcert/index')
def mitcert_index():
    return render_template('/mitcert/index.html')


@app.route('/mitcert/create')
def mitcert_create():
    return render_template('/mitcert/create')

@app.route('/mitcert/edit')
def mitcert_edit():
    return render_template('/dashboard/mitcert')






## --------------------------------------
## EXAMPLE CRUD APP
## ---------------------------------------


#index of datasets
@app.route('/examplecrud/index', methods=['GET'])
def exampleFormGet():
    
    return render_template(
        'examplecrud/index.html',
        title='Example Form Index',
        data=ExampleDataController().index()
    )              


# Creating a dataset
@app.route('/examplecrud/create', methods=['GET','POST'])
def exampleFormCreate():
    form = ExampleDataForm()
    if request.method == 'POST' and form.validate_on_submit():

        ExampleDataController().create(
            name = request.form['name'],
            text = request.form['text']
        )

        print request.form['name']
        print request.form['text']

        return redirect('examplecrud/create')
    return render_template(
                        'examplecrud/create.html', 
                        title='Example Form', 
                        form=form
                        )




@app.route('/<id>/edit', methods=['GET','POST'])
def editForm(id): #this variable is taken from the url 
    form = ExampleDataForm()

    queryid = int(id)# converts the html id into a int
    if request.method == 'POST' and form.validate_on_submit():#does it have a post method

        ExampleDataController().edit(
            id = queryid,
            name = request.form['name'],
            text = request.form['text']
        )
        return redirect('/'+id+'/edit')
  
  
    return render_template(
        'examplecrud/edit.html',
         title ='form show', 
         form = form,
         data = ExampleDataController().query(queryid) ##used to query the correct data to display
         )



@app.route('/<id>/delete', methods=['GET','POST'])
def deleteForm(id):
    queryid = int(id)
    #if request.method == 'POST':
    ExampleDataController().delete(id = queryid)
    print "delet"

    return redirect('examplecrud/index')
    


#---------------------------------------------------------