
from models import UserModel,StudentModel,LecturerModel,MitigatingCircumstanceModel
from google.appengine.ext import ndb
from google.appengine.api import users

class UserController():
	def create (self,identity,email):
		user = UserModel()
		user.identity = identity
		user.email = email
		user.user_id
		user.put()
		return user
	
	def delete(self,id_val):
		user = UserModel.get_by_id(int(id))
		return user.key.delete()


class StudentController():
	def create (self,name,email,student_number,password):
	#creates students
	#assignes the variables to the model
		student = StudentModel()
		student.name = name 
		student.email = email
		student.student_number = student_number
		student.password = password
		student.put() # 'puts' the data into the noSQL storage and generates a key 
		return student

	def edit (self,id,name,email,student_number):
		student = StudentModel.get_by_id(int(id))
		student.name = name 
		student.email = email
		student.student_number = student_number
		student.put()
		return student


	def delete(self,id_val):
		student = StudentModel.get_by_id(int(id))
		return student.key.delete()


	def index(self):	
		return StudentModel.query().fetch()


	#def deletet():
	#def query_student():
	def query(self, id):
		return StudentModel.get_by_id(int(id))

class MitigatingCircumstanceController():
	def create (self,name,email,reason):
	#creates students
	#assignes the variables to the model
		mitigatingCircumstance = MitigatingCircumstanceModel()
		mitigatingCircumstance.name = name 
		mitigatingCircumstance.email = email
		mitigatingCircumstance.reason = reason
		mitigatingCircumstance.put() 
		return mitigatingCircumstance

#	def edit_student()

#class LecturerController():
	#def create_lecturer():
	#def delete_lecturer():
	#def list_lecturer():
	#def query_subject();

#class MitigatingCircumstanceController():
	#def create_mitigatingCircumstance():
	#def delete_mitigatingCircumstance():
	#def list_mitigatingCircumstance():

#from models import StudentModel



#print StudentModel.query().fetch()
#print StudentModel.query().fetch()
#q = StudentModel.query()
#q = q.filter(StudentModel.name == Ben)


#print "howdy"
#print student
#student = StudentModel.get_by_id(5681726336532480)
#student.lecturer = 'greg'
#student.key.get()
#print student

#student.key.delete()
#print student
#print "did it work?"
