#Models for the noSQL database 
from google.appengine.ext import ndb
from flask_login import UserMixin

class UserModel(ndb.Model): #google noSQL model creation   
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()

class PostsModel(ndb.Model):
    title = ndb.StringProperty()
    body = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty()

class User(UserMixin, ndb.Model): # this is the flask-login model
    user_email = ndb.StringProperty(required=True, indexed=True)
    user_password = ndb.StringProperty(required=True)


class ExampleDataModel(ndb.Model):
    name = ndb.StringProperty()
    text = ndb.StringProperty()
