import webapp2
import cgi
import jinja2
import os

from authomatic import Authomatic
from authomatic.adapters import Webapp2Adapter
from config import CONFIG

from google.appengine.ext import ndb
from google.appengine.api import users

from controllers import *

#from models import StudentModel, CourseModel

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
authomatic = Authomiatic(confif=CONFIG, secret='some random string')


class LoginPage(webapp2.RequestHandler):   
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render())
        
    def post(self):
        UserController().create(
            identity = self.request.get('InputName'), 
            email = self.request.get('InputEmail'), 
            password = self.request.get('InputStudentPassword'),
        )
        self.response.out.write("/login")
    


class Login(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render())


class LoginTest(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            template = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            template = '<a href="{}">Sign in</a>'.format(login_url)
   

        self.response.write(
            '<html><body>{}</body></html>'.format(template))

class StudentIndex(webapp2.RequestHandler):
    
    def get(self):
        user = users.get_current_user()
        if user: 
            template = jinja_environment.get_template('templates/students/index.html')
            template_values = {
                'user': user.nickname(),
                'logouturl': users.create_logout_url('/'),
                'students': StudentController().index(), 
            }
            self.response.out.write(template.render(template_values))
        else:
            self.redirect("/")
            
        
        
    
class StudentCreate(webapp2.RequestHandler):   
    def get(self):
    
        template = jinja_environment.get_template('templates/students/create.html')
        self.response.out.write(template.render())
        
    def post(self):
        StudentController().create(
            name = self.request.get('InputName'), 
            email = self.request.get('InputEmail'), 
            student_number = self.request.get('InputStudentNumber'), 
            password = self.request.get('InputStudentPassword'),
        )
        self.redirect("/students")
        
class StudentShow(webapp2.RequestHandler):     
    def get(self, id):
        
        
        template = jinja_environment.get_template('templates/students/show.html')
        template_values = {
            'student': StudentController().query(id),
            
        }
        self.response.out.write(template.render(template_values))

class StudentEdit(webapp2.RequestHandler):
    def post(self, id):
        StudentController().edit(
            id = self.request.get('InputID'),
            name = self.request.get('InputName'), 
            email = self.request.get('InputEmail'), 
            student_number = self.request.get('InputStudentNumber'),
        )
        redirecting_url = "/students/" + self.request.get('InputID')
        self.redirect(redirecting_url)





class UserCreate(webapp2.RequestHandler): 
    user = users.get_current_user()  
    def get(self):    
        template = jinja_environment.get_template('templates/students/createUser.html')
        self.response.out.write(template.render())
        
    def post(self):
        UserController().create(
            identity = self.request.get('InputName'), 
            email = self.request.get('InputEmail'),  
        )
        self.redirect("/students")

class LoginAutho(webapp2.RequestHandlfrom flask_login import LoginManager, current_user, login_userer):
    def any(self,provider_name):

        result = authomatic.login(Webapp2Adapter(self),provider_name)

        if result:
            self.response.out.write('<a href="..">Home</a>')
        if result.error:
            self.response.write(u'<h2>Damn that error: {}</h2>'.format(result.error.message))
        elif result.user:
            if not (result.user.name and result.user.id):
                result.user.update()

