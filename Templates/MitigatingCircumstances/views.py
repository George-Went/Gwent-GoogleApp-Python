import webapp2
import cgi
import jinja2
import os

from controllers import *

from google.appengine.ext import ndb

#from models import StudentModel, CourseModel

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))




class StudentIndex(webapp2.RequestHandler):
    def get(self):
        
        template = jinja_environment.get_template('templates/students/index.html')

        template_values = {
            'students': StudentController().index()
        }

        self.response.out.write(template.render(template_values))
    
class StudentCreate(webapp2.RequestHandler):   
    def get(self):
    
        template = jinja_environment.get_template('templates/students/create.html')
        self.response.out.write(template.render())
        
    def post(self):
        StudentController().create(
            name = self.request.get('InputName'), 
            lecturer = self.request.get('InputLecturer'), 
            email = self.request.get('InputEmail'), 
            student_number = self.request.get('InputStudentNumber'), 
        )
        self.redirect("/students")
        #self.response.out.write(student)
        
class StudentShow(webapp2.RequestHandler):   
    def get(self, id):
    
        template = jinja_environment.get_template('templates/students/show.html')
        template_values = {
            'student': StudentController().query(id)
        }
        self.response.out.write(template.render(template_values))

class StudentEdit(webapp2.RequestHandler):
    def post(self, id):
        StudentController().edit(
            id = self.request.get('InputID'),
            name = self.request.get('InputName'), 
            lecturer = self.request.get('InputLecturer'), 
            email = self.request.get('InputEmail'), 
            student_number = self.request.get('InputStudentNumber'),
        )
        redirecting_url = "/students/" + self.request.get('InputID')
        self.redirect(redirecting_url)
    