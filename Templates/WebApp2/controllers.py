
from models import StudentModel
from google.appengine.ext import ndb


class Student(object):
    def create_student (self,first_name,last_name,username,student_number)
        #creates students
            
        StudentModel.first_name = first_name
        StudentModel.last_name = last_name
        StudentModel.username = username
        StudentModel.student_number
        StudentModel.put()

   def delete_student()
        student_query = StudentModel.all()
        return 