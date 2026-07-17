import json


class StudentManager:

    def __init__(self):
        self.file = "data/students.json"


    def load_courses(self):

        try:
            with open(self.file, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("courses.json is corrupted.")
            return []


    def save_students(self, students):
        with open(self.file, "w") as file:
            json.dump(students, file, indent=5)


    def add_student(self, student):

        students = self.load_student()


        for old_student in students:

            if old_student["student_id"] == student.student_id:
                return False


        students.append(student.to_dict())

        self.save_students(students)

        return True



    def view_students(self):
        students = self.load_student()

        for student in students:
            print(
            f"""
            Name: {student['name']}
            Age: {student['age']}
            ID: {student['student_id']}
            Department: {student['department']}
            GPA: {student['GPA']}
            --------------------""")




    def search_student(self,student_id):
        students=self.load_student()

        for student in students:
            if student["student_id"]==student_id :
                return student
        

        return None


    def update_student(self, student_id, new_data):

        students = self.load_student()

        for student in students:

            if student["student_id"] == student_id:

                student.update(new_data)

                self.save_students(students)

                return True

        return False
    

    def delete_student(self, student_id):

        students = self.load_student()

        for student in students:

            if student["student_id"] == student_id:

                students.remove(student)

                self.save_students(students)

                return True

        return False