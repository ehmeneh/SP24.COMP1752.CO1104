from student import Student

class StudentManagement:
    """
    1. __init__
    2. add_student
    3. search_student
    4. remove_student
    """
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


student_management = StudentManagement();
print(student_management.students)

student1 = Student("John", 22, 55)
student_management.add_student(student1)
print()


