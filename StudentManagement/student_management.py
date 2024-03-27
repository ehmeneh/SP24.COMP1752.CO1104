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

    def search_student(self, name):
        found_students = []
        for student in self.students:
            if student.name == name:
                found_students.append(student)
        return found_students

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return "Student removed successfully."
        return "Student not found in the database."


student_management = StudentManagement();

student1 = Student("John", 22, 55)
student2 = Student("David", 20, 75)
student3 = Student("Nancy", 21, 85)

student_management.add_student(student1)
student_management.add_student(student2)
student_management.add_student(student3)

result = student_management.search_student("John")
removed_result = student_management.remove_student("John")

print(removed_result)


