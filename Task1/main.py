from Student import Student
from Course import Course

from manag.Student_manager import StudentManager
from manag.Course_manager import CourseManager
from manag.Enrollment_manager import EnrollmentManager
from manag.Report_manager import ReportManager


student_manager = StudentManager()
course_manager = CourseManager()
enrollment_manager = EnrollmentManager()
report_manager = ReportManager()



def add_student():

    name = input("Enter name: ")

    while True:
        try:
            age = int(input("Enter age: "))

            if age <= 0:
                print("❌ Age must be greater than 0.")
                continue

            break

        except ValueError:
            print("❌ Please enter a valid age.")

    while True:
        try:
            student_id = int(input("Enter ID: "))

            if student_id <= 0:
                print("❌ ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("❌ Please enter a valid ID.")

    department = input("Enter department: ")

    while True:
        try:
            gpa = float(input("Enter GPA: "))

            if 0 <= gpa <= 4:
                break

            print("❌ GPA must be between 0 and 4.")

        except ValueError:
            print("❌ Please enter a valid GPA.")

    student = Student(
        name,
        age,
        student_id,
        department,
        gpa
    )

    result = student_manager.add_student(student)

    if result:
        print("Student added successfully ✅")
    else:
        print("Student ID already exists ❌")



def search_student():

    while True:
        try:
            student_id = int(input("Enter Student ID: "))

            if student_id <= 0:
                print("❌ ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("❌ Please enter a valid ID.")

    student = student_manager.search_student(student_id)

    if student:
        print(f"""
Name: {student['name']}
Age: {student['age']}
ID: {student['student_id']}
Department: {student['department']}
GPA: {student['GPA']}
""")
    else:
        print("Student not found ❌")





def delete_student():

    while True:
        try:
            student_id = int(input("Enter Student ID: "))

            if student_id <= 0:
                print("❌ ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("❌ Please enter a valid ID.")

    result = student_manager.delete_student(student_id)

    if result:
        print("Deleted successfully ✅")
    else:
        print("Student not found ❌")




def add_course():

    name = input("Course name: ")
    course_id = input("Course ID: ")

    while True:
        try:
            hours = int(input("Course hours: "))

            if hours <= 0:
                print("❌ Hours must be greater than 0.")
                continue

            break

        except ValueError:
            print("❌ Please enter a valid number.")

    course = Course(
        name,
        course_id,
        hours
    )

    result = course_manager.add_course(course)

    if result:
        print("Course added successfully ✅")
    else:
        print("Course ID already exists ❌")


def view_courses():

    course_manager.view_courses()




def enroll_student():

    while True:
        try:
            student_id = int(input("Student ID: "))

            if student_id <= 0:
                print("❌ ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("❌ Please enter a valid ID.")

    course_id = input("Course ID: ")

    student_data = student_manager.search_student(student_id)

    if student_data is None:
        print("Student not found ❌")
        return

    student = Student(
        student_data["name"],
        student_data["age"],
        student_data["student_id"],
        student_data["department"],
        student_data["GPA"]
    )

    courses = course_manager.load_courses()

    for course in courses:

        if course["course_id"] == course_id:

            course_object = Course(
                course["name"],
                course["course_id"],
                course["hours"]
            )

            result = enrollment_manager.enroll(
                student,
                course_object
            )

            if result:
                print("Enrollment done ✅")
            else:
                print("Student already enrolled in this course ❌")

            return

    print("Course not found ❌")



def reports():

    print("""
====================
Reports
====================

1. Count Students
2. Average GPA
3. Highest GPA
4. Students per Department
""")


    choice = input("Choose: ")



    if choice == "1":

        print(
            "Number of students:",
            report_manager.count_students()
        )


    elif choice == "2":

        print(
            "Average GPA:",
            report_manager.average_gpa()
        )


    elif choice == "3":

        student = report_manager.highest_gpa()

        print(student)



    elif choice == "4":

        result = report_manager.students_per_department()

        for dep, count in result.items():

            print(
                f"{dep}: {count} students"
            )





def menu():

    while True:

        print("""
=========================
 Student Management
=========================

1. Add Student
2. View Students
3. Search Student
4. Delete Student

5. Add Course
6. View Courses
7. Enroll Student

8. Reports

0. Exit
=========================
""")


        choice = input("Choose: ")




        if choice == "1":

            add_student()



        elif choice == "2":

            student_manager.view_students()



        elif choice == "3":

            search_student()



        elif choice == "4":

            delete_student()



        elif choice == "5":

            add_course()



        elif choice == "6":

            view_courses()



        elif choice == "7":

            enroll_student()



        elif choice == "8":

            reports()



        elif choice == "0":

            print("Good Bye 👋")
            break



        else:

            print("Invalid choice ❌")





menu()