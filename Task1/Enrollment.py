from Student import Student
from Course import Course

class Enrollment :
    def __init__(self,Student,Course):
        self.Student=Student
        self.Course=Course
        self.grade=None



    def set_grade(self, grade):
        self.grade = grade

