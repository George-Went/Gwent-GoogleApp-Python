
from models import PersonModel,StudentModel,LecturerModel,MitigatingCircumstanceModel
from google.appengine.ext import ndb



class StudentController():
	def create (self,name,lecturer,email,student_number):
	#creates students
	#assignes the variables to the model
		student = StudentModel()
		student.name = name 
		student.lecturer = lecturer
		student.email = email
		student.student_number = student_number
		StudentModel.put() # 'puts' the data into the noSQL storage and generates a key 






	def index(self):
		return StudentModel.all()


	#def deletet():
	#def query_student():


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