

from flask_login import LoginManager, current_user, login_user

from google.appengine.ext import ndb
from google.appengine.api import users

from models import UserModel, PostsModel, ExampleDataModel

class UserController():
	def create (self,name,email,password):
		user = UserModel()
		user.name = name
		user.email = email
		user.password = password
		user.put()
		return user
	





class ExampleDataController():
	def create (self,name,text):
	#creates students
	#assignes the variables to the model
		exampleData = ExampleDataModel() #speuserusercifies the creation of a new dataset
		exampleData.name = name #links the data to the importted vars
		exampleData.text = text
		exampleData.put() # 'puts' the data into the noSQL storage and generates a key 
		return exampleData

	def edit (self,id,name,text):
		exampleData = ExampleDataModel.get_by_id(int(id)) #the dataset is slected based on its id
		exampleData.name = name 
		exampleData.text = text
		exampleData.put()
		return exampleData


	def delete(self,id):
		exampleData = ExampleDataModel.get_by_id(int(id))
		return exampleData.key.delete()


	def index(self):	
		return ExampleDataModel.query().fetch() # returns all of type exampledatamodel

	def query(self, id):
		return ExampleDataModel.get_by_id(int(id))
		# for queries you can also use ExampleDataModel.query(ExampleDate.name == "obi wa")

		
##Login in Users using Flask-Login

#Mock database 
users = {'foo@bar.tld': {'password': 'secret'}}


# @login.user_loader
# def load_user(id):
# 	return User.Query.get(int(id))