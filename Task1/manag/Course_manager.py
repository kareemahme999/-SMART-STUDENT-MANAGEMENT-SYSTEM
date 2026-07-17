import json


class CourseManager:

    def __init__(self):
        self.file = "data/courses.json"


    def load_courses(self):

        try:
            with open(self.file, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("courses.json is corrupted.")
            return []

    def save_courses(self, courses):
        with open(self.file, "w") as file:
            json.dump(courses, file, indent=4)


    def add_course(self, course):

        courses = self.load_courses()


        for old_course in courses:

            if old_course["course_id"] == course.course_id:

                return False


        courses.append({
            "course_id": course.course_id,
            "name": course.name,
            "hours": course.hours
        })


        self.save_courses(courses)

        return True

    def view_courses(self):

        courses = self.load_courses()


        for course in courses:

            print(
            f"""
    Name: {course['name']}
    ID: {course['course_id']}
    Hours: {course['hours']}
    --------------------
    """
            )