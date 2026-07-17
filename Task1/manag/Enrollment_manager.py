import json

class EnrollmentManager:

    def __init__(self):
        self.file = "data/enrollments.json"


    def load_enrollments(self):

        try:
            with open(self.file, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("enrollments.json is corrupted.")
            return []


    def save_enrollments(self, enrollments):
        with open(self.file, "w") as file:
            json.dump(enrollments, file, indent=4)


    def enroll(self, student, course):

        enrollments = self.load_enrollments()


        for old_enrollment in enrollments:

            if (
                old_enrollment["student_id"] == student.student_id
                and
                old_enrollment["course_id"] == course.course_id
            ):

                return False



        enrollment = {

            "student_id": student.student_id,

            "course_id": course.course_id

        }


        enrollments.append(enrollment)
        self.save_enrollments(enrollments)


        return True


    

    def load_courses(self):

        with open("data/courses.json", "r") as file:
            return json.load(file)
        

    def get_student_courses(self, student_id):

        enrollments = self.load_enrollments()
        courses_data = self.load_courses()

        student_courses = []


        for enrollment in enrollments:

            if enrollment["student_id"] == student_id:

                for course in courses_data:

                    if course["course_id"] == enrollment["course_id"]:

                        student_courses.append(course["name"])


        return student_courses