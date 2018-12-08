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
    
    
    

