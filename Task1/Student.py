from Person import Person
class Student(Person):
    def __init__(self,name,age,student_id, department ,GPA):
        super().__init__(name,age)
        self.student_id=student_id
        self.department=department
        self.GPA=GPA
        self.courses=[]
    def add_course(self,course):
        self.courses.append(course)
 

  ## test
    def display_info(self):
        print(
    f"""
    Name:{self.name}
    Age: {self.age}
    ID: {self.student_id}
    Department: {self.department}
    GPA: {self.GPA}
    """
        )
    


    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "student_id": self.student_id,
            "department": self.department,
            "GPA": self.GPA
        }






