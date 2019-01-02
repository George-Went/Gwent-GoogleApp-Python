

# Flask Imports 
from flask import Flask, render_template, request, redirect, flash, url_for

# Flask-Login Imports
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin

# Flask-WTF Imports 
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, ValidationError, DataRequired, Email, EqualTo

# GAE imports 
from config import Config

#from models import User
from forms import *
from controllers import  *
from models import *

#Models for the noSQL database 





app = Flask(__name__)
app.config.from_object(Config)


app.config['SECRET_KEY'] = 'hello'


csrf = CSRFProtect(app)



# --------------------------------------------
# GENERATING TEST DATA 
# --------------------------------------------

@app.route('/generatedata')
def generatedata():
    # exampleUser = User()
    # exampleUser.name = "George" #specifies the creation of a new dataset
    # exampleUser.email = "gep.went@gmail.com" #links the data to the importted vars
    # exampleUser.password = "password"
    # exampleUser.put()

    # exampleUser2 = User() #specifies the creation of a new dataset
    # exampleUser2.name = "Mark"
    # exampleUser2.email = "mark@gmail.com" #links the data to the importted vars
    # exampleUser2.password = "password"
    # exampleUser2.put()

    # UserController()

    # MitigatingCircumstanceController().create(
    #     student = "Mark",
    #     student_email = "mark@gmail.com",
    #     unit = "Data Mining",
    #     title = "Working out Nearest Neigbour",
    #     reason = "Hi sir, im having issues with working out how nearest neighbour works, please advise",
    #     state = 1
    # )

    # MitigatingCircumstanceController().create(
    #     student = "John",
    #     student_email = "john@btinternet.com",
    #     unit = "Networks",
    #     title = "Ping system",
    #     reason = "How do i ping a server",
    #     state = 1
    # # )
    # unitArray = ['maths','history']
    # print unitArray

    # exampleStaff = StaffModel()
    # unit = UnitModel()
    # exampleStaff.name = "Dave"
    # exampleStaff.email = "dave@gmail.com"
    # exampleStaff.units =[unit.name='maths'),unit(name='hsitory')]
    
    # exampleStaff.put()

    queryunit = UnitModel()

    exampleStaff = StaffModel(name ='Dave',email='dave@gmail.com',
                            units=[UnitModel(name='history'),
                                    UnitModel(name='maths')])
    exampleStaff.put()

    print "UNIT: " + str(queryunit.query().fetch())


    # UnitController().create(
    #     name = "history"
    # )
    # UnitController().create(
    #     name = "biology"
    # )
    
    # exampleStaff = StaffModel()
    # exampleStaff.name = "dave"
    # exampleStaff.email = "dave@gmail.com"
    # exampleStaff.units[1] = "maths"
    # exampleStaff.units[2] = "history"
    # exampleStaff.put()
    flash('data added')
    return redirect('/')




## ---------------------------------------
## LOGIN SYSTEM
## ---------------------------------------

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


#login use reloads an object when a user loads a new page 
@login_manager.user_loader 
def load_user(email):
    return User.query().filter(User.email==email).get()

@app.route('/')
def index():
    print "CURRENT USER: " + str(current_user)
    return render_template('index.html')

## LOGIN PAGE --------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit(): ## if the form is submitted with the correct data
        name = form.email.data
        text = form.password.data
        
        print name
        print text
        
        check = form.email.data
        #get User data based on the email address entered
        user = User.query(User.email == check).get()
        if user:
            if user.password == form.password.data:
                login_user(user)
                return redirect(url_for('dashboard'))
        
        return "<h1>Invalid username or password</h1>"
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
    return redirect(url_for('login'))

@app.route('/user')
@login_required
def checkuser():

    print "the user is: " + current_user.name
    return "The current user is: " + current_user.name + " " + current_user.email


## ---------------------------------------
## CREATE USER SYSTEM
## ---------------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():   


    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():


        UserController().create(
            name = request.form['name'],
            email = request.form['email'],
            password = request.form['password'],

        )

        print request.form['name']
        print request.form['email']
        print request.form['password']



        return redirect('/login')

    return render_template('login/signup.html')





## ---------------------------------------
## STUDENTS SYSTEM 
## --------------------------------------- 
@app.route('/dashboard')
@login_required
def dashboard():
    print current_user.email
    query = MitigatingCircumstanceController().index()
    print "CURRENT USER: " + str(current_user.email)
    queryemail = MitigatingCircumstanceController().querybyemail(current_user.email)
    #querires based on the current user logged in
    print "QUERY ALL: " + str(query)
    print "QUERY EMAIL: "  + str(queryemail)
   # print queryemail.student_email
    


    return render_template(
    '/dashboard.html',
    title='Example Form Index',
    MitigatingCircumstances = queryemail
       )  

    
##-------------------------------------------
## SUBMITTING MITIGATING CIRCUMSTANCES
##-------------------------------------------

@app.route('/submit_mitcert', methods=['GET','POST'])
def submitMitigatingCircumstance():
    form = MitigatingCircumstanceForm()

    if request.method == 'POST' :

        student = current_user.name
        student_email = current_user.email
        unit = request.form['unit']
        title = request.form['title']
        reason = request.form['reason']
        state = 1
        
        print student
        print student_email
        print unit
        print title
        print reason
        print state

        MitigatingCircumstanceController().create(
            student = current_user.name,
            student_email = current_user.email,
            unit = request.form['unit'],
            title = request.form['title'],
            reason = request.form['reason'],
            state = 1
        )
        return redirect('/dashboard')

    return render_template(
                        'mitcert/create.html', 
                        title='Mitigating circumstance Form', 
                        form=form
                        )


@app.route('/<id>/edit', methods=['GET','POST'])
def editMitigatingCircumstance(id): #this variable is taken from the url 
    form = MitigatingCircumstanceForm()

    queryid = int(id)# converts the html id into a int
    query_mitcert = MitigatingCircumstanceController().querybyid(queryid)

    print query_mitcert.student_email
    print query_mitcert.reason

    if request.method == 'POST' and form.validate_on_submit():#does it have a post method

        MitigatingCircumstanceController().edit(
            id = queryid,
            student = current_user.name,
            student_email = current_user.email,
            unit = request.form['unit'],
            title = request.form['title'],
            reason = request.form['reason'],
            state = 1
        )
        return redirect('/dashboard')
  
  
    return render_template(
        'mitcert/edit.html',
         title ='form show', 
         form = form,
         data = query_mitcert
         )





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
    

