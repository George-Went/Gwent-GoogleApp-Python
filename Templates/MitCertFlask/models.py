#Models for the noSQL database 
from google.appengine.ext import ndb

class UserModel(ndb.Model): #google noSQL model creation   
    email = ndb.StringProperty()
    identity = ndb.StringProperty()
    user_id = ndb.StringProperty()

    @classmethod
    def get_by_user(cls, user):
        return cls.query().filter(cls.user_id == user.user_id()).get()
    
class StudentModel(ndb.Model): #google noSQL model creation  
    name = ndb.StringProperty()
    email = ndb.StringProperty()    
    student_number = ndb.StringProperty()
    password = ndb.StringProperty()

class LecturerModel(ndb.Model): #google noSQL model creation   
    name = ndb.StringProperty()
    subject = ndb.StringProperty()
    email = ndb.StringProperty()

class MitigatingCircumstanceModel(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    reason = ndb.StringProperty()
