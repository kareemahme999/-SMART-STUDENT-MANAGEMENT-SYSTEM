import json


class ReportManager:

    def __init__(self):
        self.file = "data/students.json"


    def load_students(self):

        with open(self.file, "r") as file:
            return json.load(file)

## to count main 
    def count_students(self):

        students = self.load_students()

        return len(students)
    

    def average_gpa(self):

        students = self.load_students()

        total = 0

        for student in students:
            total += student["GPA"]

        if len(students) == 0:
            return 0

        return total / len(students)
    





    def highest_gpa(self):

        students = self.load_students()

        if len(students) == 0:
            return None


        highest_student = students[0]


        for student in students:

            if student["GPA"] > highest_student["GPA"]:
                highest_student = student


        return highest_student
    



    def students_per_department(self):

        students = self.load_students()

        departments = {}


        for student in students:

            department = student["department"]


            if department in departments:
                departments[department] += 1

            else:
                departments[department] = 1


        return departments