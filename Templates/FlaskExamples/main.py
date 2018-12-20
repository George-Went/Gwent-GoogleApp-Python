#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_wtf import FlaskForm, CSRFProtect

from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from google.appengine.ext import ndb

from forms import LoginForm, ExampleDataForm
from config import Config
#from models import User
from controllers import UserController, ExampleDataController 





app = Flask(__name__)
app.config.from_object(Config)
#login_manager = LoginManager()
#login_manager.init_app(app)


app.config['SECRET_KEY'] = 'you-will-never-guess'
csrf = CSRFProtect(app)

@app.route('/')
@app.route('/index')
def index():
    # user = {'username': 'George'}
    # posts = [
    #     {
    #         'author': {'username': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'username': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     }
    # ]
    return redirect('/examplecrud/index')
  #  return render_template('index.html', title='George', user=user, posts=posts)


@app.route('/helloworld')
def hello_world():
    return render_template("index.html")

@app.route('/george')
def george():
    user = {'username': 'George'}
    return '''
            <html>
                <head>
                    <title>Home Page - Microblog</title>
                </head>
                <body>
                    <h1>Hello, ''' + user['username'] + '''!</h1>
                </body>
            </html>
            '''

@app.route('/georgetemplate')
def GeorgeTemplate():
    user = {'username': 'George'}
    return render_template('George.html', title='Home', user=user)










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
    


#---------------------------------------------------------



#@app.route('/(\d+)/delete')



# Login and Logout Funcitons

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index')) #if the user is already logged in, they return to the index page
#     form = LoginForm()
#     if form.validate_on_submit():

#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember_me.data)

#         return redirect(url_for('index'))
#     return render_template('login.html', title='Sign In', form=form)

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))