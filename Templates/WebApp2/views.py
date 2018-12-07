import webapp2
import cgi
import jinja2
import os

from google.appengine.ext import ndb

#from models import StudentModel, CourseModel

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class MainPage(webapp2.RequestHandler):
    def get(self):
        
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render())



class George(webapp2.RequestHandler):
    def get(self):
        name = "george"
        message = '<p>Hello %s</p>'  % name
        self.response.out.write(message)




class Me(webapp2.RequestHandler):
    def get(self): 
        template = jinja_environment.get_template('templates/form.html')
        context = {
            'name': "George",
            'lecturer': "Tim",
            'issue': "cant do REST",
            'comment': "halp",
        } 
        self.response.out.write(template.render(context))



class Form(webapp2.RequestHandler):
    def get(self): 
        template = jinja_environment.get_template('templates/form.html')

        context = {
            'name': "George",
            'lecturer': "lecturer",
            'issue': "dsfsdfsd",
            'comment': "commsdfdsfdsfdsent",
        } 
        self.response.out.write(template.render(context))

class StudentModel(ndb.Model): #google noSQL model creation   
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    username = ndb.StringProperty()
    student_number = ndb.StringProperty()


class CreateStudent(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/createStudent.html')

        template_values = {
            'first_name ': self.request.get('first_name'),
            'last_name ': self.request.get('last_name'),
            'username ': self.request.get('username'),
            'student_number ': self.request.get('student_number'),
        }

        self.response.out.write(template.render(template_values))

    def post(self):
        
        StudentModel.first_name = self.request.get('first_name'),
        StudentModel.first_name = self.request.get('last_name'),
        StudentModel.first_name = self.request.get('username'),
        StudentModel.first_name = self.request.get('student_number'),
        StudentModel.put()

        

class CreateStudentController(webapp2.RequestHandler):   
  
    def post(self):#HTTP post data from form page 
        template = jinja_environment.get_template('templates/submitted_form.html')
        StudentModel.first_name = self.request.get('first_name'),
        StudentModel.last_name = self.request.get('last_name'),
        StudentModel.username = self.request.get('username'),
        StudentModel.student_number = self.request.get('student_number'),
        
        submission = S + "Mitigating_Circumstances"
        
        

        submission = Student(student_name=self.request.get('name'))
        submission.put()

        
        template_values = {
            'first_name ': self.request.get('first_name'),
            'last_name ': self.request.get('last_name'),
            'username ': self.request.get('username'),
            'student_number ': self.request.get('student_number'),
        }
        self.response.out.write(template.render(context))
    def get(self): #HTTP GET data from form page 
       
       
        

        name = self.request.get('name')

          #writes the ( gets the ( /form 'name ))



class Submit(webapp2.RequestHandler):   
  
    def post(self):#HTTP post data from form page 
        template = template_env.get_template('templates/submitted_form.html')
        name = self.request.get('name')
        
        submission = name + "Mitigating_Circumstances"
        


        submission = Student(student_name=self.request.get('name'))
        submission.put()

        context = {
            'name' : self.request.get('name'),
        }
        self.response.out.write(template.render(context))
    def get(self): #HTTP GET data from form page 
       
       
        

        name = self.request.get('name')

          #writes the ( gets the ( /form 'name ))





class FormExample(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/SubmitExample" method="post">
                <div><textarea name="content" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="Sign Guestbook"></div>
              </form>
            </body>
          </html>""")







class SubmitExample(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(cgi.escape(self.request.get('content')))
        self.response.out.write('</pre></body></html>')


