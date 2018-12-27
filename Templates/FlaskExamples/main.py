#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_wtf import FlaskForm, CSRFProtect
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.contrib.google import make_google_blueprint, google 

from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired

from google.appengine.ext import ndb

from forms import  ExampleDataForm
from config import Config
#from models import User
from controllers import UserController, ExampleDataController 





app = Flask(__name__)
app.config.from_object(Config)


app.config['SECRET_KEY'] = 'hello'


csrf = CSRFProtect(app)
google_blueprint = make_google_blueprint(client_id='',client_secret='')
twitter_blueprint = make_twitter_blueprint(api_key ='', api_secret='')
# api key = 
#api seceret = 
github_blueprint = make_github_blueprint(client_id='', client_secret='')

app.register_blueprint(twitter_blueprint, url_prefix='')

#TO BE REMOVED
#Models for the noSQL database 
from google.appengine.ext import ndb
from flask_login import UserMixin

# --------------------------------------------
# GENERATING TEST DATA 
# --------------------------------------------

@app.route('/generateuser')
def generateuser():
    exampleUser = User()
    exampleUser.name = "George" #specifies the creation of a new dataset
    exampleUser.email = "gep.went@gmail.com" #links the data to the importted vars
    exampleUser.password = "password"
    exampleUser.put()

    exampleUser2 = User() #specifies the creation of a new dataset
    exampleUser2.name = "Mark"
    exampleUser2.email = "mark@gmail.com" #links the data to the importted vars
    exampleUser2.password = "password"
    exampleUser2.put()
    return redirect('/')


## ---------------------------------------
## LOGIN SYSTEM
## ---------------------------------------

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember Me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = StringField('Username', validators=[InputRequired()])
   
# User model is used to store used data 
class User(UserMixin, ndb.Model): #google noSQL model creation   
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False




#login use reloads an object when a user loads a new page 
@login_manager.user_loader 
def load_user(email):
    return User.query().filter(User.email==email).get()

@app.route('/')
def index():
    return render_template('index.html')

#login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit(): ## if the form is submitted with the correct data
        name = form.email.data
        text = form.password.data
        
        print name
        print text
        
        check = form.email.data
        #get user based on the email address entered
        user = User.query(User.email == check).get()
        if user:
            if user.password == form.password.data:
                login_user(user)
                return "<h1>user: " + str(current_user.email) +"</h1>"
        
        return "<h1>Invalid username or password</h1>"

        # print userObj
        # print userObj.key
        # login_user(userObj)
        
        #return '<h1>' + form.email.data + ' ' + form.password.data +'</h1>' 
    else:
        print "nope"
        print form.email.data
        print form.password.data
        return render_template('login/login.html', form = form)
    return render_template('login/login.html', form = form)

# Logout function
@app.route('/logout')
@login_required
def logout():
    logout_user()
    print "you are now logged out"
    return "you are now logged out"

@app.route('/user')
@login_required
def checkuser():

    print "the user is: " + current_user.name
    return "The current user is: " + current_user.name 




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit(): ## if the form is submitted with the correct data
        return '<h1>' + form.email.data + ' ' + form.password.data +'</h1>' 
    else:
        return 
    return render_template('login/signup.html', form = form)


#------------------------------------------

## ---------------------------------------
## STUDENTS SYSTEM 
## ---------------------------------------

@app.route('/dashboard')
def dashboard():
        return render_template(
        'examplecrud/index.html',
        title='Example Form Index',
        data=ExampleDataController().index()
    )  

@app.route('/submitMitigatingCircumstance ')
def submitMitigatingCircumstance():
    return render_template('dashboard.html')

@app.route('/')
# check if admin (wont be admin hopefully
    #check student id
        #display students mit cert

## ---------------------------------------
## LECTURER SYSTEM 
## ---------------------------------------

@app.route('/dashboard')
def admindashboard():
    #check if admim
        #check name of admin
            #display students mit cert
    #if not, go to 

    return render_template(
        'examplecrud/index.html',
        title='Example Form Index',
        data=ExampleDataController().index()
    )   

@app.route('/submitMitigatingCircumstance ')
def adminMitigatingCircumstance():
    return render_template('dashboard.html')

@app.route('/')

## ---------------------------------------
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
    

