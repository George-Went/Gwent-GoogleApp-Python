
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
		student.put() # 'puts' the data into the noSQL storage and generates a key 
		return student

	def edit (self,id,name,lecturer,email,student_number):
		student = StudentModel.get_by_id(int(id))
		student.name = name 
		student.lecturer = lecturer
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
