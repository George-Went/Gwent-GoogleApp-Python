#Models for the noSQL database 
from google.appengine.ext import ndb

class PersonModel(ndb.Model): #google noSQL model creation   
    ID = ndb.StringProperty()

class StudentModel(ndb.Model): #google noSQL model creation   
    name = ndb.StringProperty()
    lecturer = ndb.StringProperty()
    email = ndb.StringProperty()
    student_number = ndb.StringProperty()

class LecturerModel(ndb.Model): #google noSQL model creation   
    name = ndb.StringProperty()
    subject = ndb.StringProperty()
    email = ndb.StringProperty()

class MitigatingCircumstanceModel(ndb.Model): #google noSQL model creation   
    student = ndb.StringProperty()
    lecturer = ndb.StringProperty()
    assignment = ndb.StringProperty()
    issue = ndb.StringProperty()
    resolved = ndb.BooleanProperty()