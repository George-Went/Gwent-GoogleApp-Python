#Models for the noSQL database 
from google.appengine.ext import ndb

class StudentModel(ndb.Model): #google noSQL model creation   
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    username = ndb.StringProperty()
    student_number = ndb.StringProperty()
