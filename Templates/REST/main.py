import webapp2
import cgi
import jinja2
import os

from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class Main(webapp2.RequestHandler):
    def get(self):
        
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render())

class PersonModel(ndb.Model): #google noSQL model creation   
    name = ndb.StringProperty()
    address = ndb.StringProperty()
    phone = ndb.StringProperty()
    DOB = ndb.StringProperty() 

class Form(webapp2.RequestHandler):
    def get(self): #equal to request.merthod = GET
        


        template = jinja_environment.get_template('templates/form.html')

        template_values = {
            'name ': self.request.get('name'),
            'address ': self.request.get('address'),
            'phone ': self.request.get('phone'),
            'dob ': self.request.get('dob'),
        }
        
        self.response.out.write(template.render(template_values))


class SubmitForm(webapp2.RequestHandler):

    def post(self): 
        person = PersonModel()
        
        person.name = self.request.get('name')
        person.address = self.request.get('address')
        person.phone = self.request.get('phone')
        person.DOB = self.request.get('dob')
        person.put() # THis is where ID's for keys are assigned 

    def get(self):
        template = jinja_environment.get_template('templates/Submit_Form.html')

        template_values = {
            'name ': self.request.get('name'),
            'address ': self.request.get('address'),
            'phone ': self.request.get('phone'),
            'dob ': self.request.get('dob'),
        }

        self.response.out.write(template.render(template_values))


class ViewPeople(webapp2.RequestHandler):

    def get(self):


       result = q.filter()
        
        print listallQuery

        for entity in listallQuery:
            name = PersonModel.name
            address = PersonModel.address
            phone = PersonModel.phone
            dob = PersonModel.DOB


            template = jinja_environment.get_template('templates/form.html')
            template_values = {
                'name ': self.request.get('name'),
                'address ': self.request.get('address'),
                'phone ': self.request.get('phone'),
                'dob ': self.request.get('dob'),

            }

        self.response.out.write(template.render(template_values))

class ViewPeople(webapp2.RequestHandler):
   # def query(ancestor_key):
    #    return 
    def get(self):


       result = q.filter()
        
        print listallQuery

        for entity in listallQuery:
            name = PersonModel.name
            address = PersonModel.address
            phone = PersonModel.phone
            dob = PersonModel.DOB


            template = jinja_environment.get_template('templates/form.html')
            template_values = {
                'name ': self.request.get('name'),
                'address ': self.request.get('address'),
                'phone ': self.request.get('phone'),
                'dob ': self.request.get('dob'),

            }

        self.response.out.write(template.render(template_values))



application = webapp2.WSGIApplication(
[
    ('/', Main),
    ('/Form', Form),
    ('/SubmitForm',SubmitForm),
    ('/ViewPeople',ViewPeople),

],debug=True)