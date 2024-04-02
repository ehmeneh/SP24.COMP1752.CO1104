from student import Student
from student_management import StudentManagement

def test_add_student():
    management = StudentManagement()
    student1 = Student("John", 22, 55)
    management.add_student(student1)
    assert len(management.students) == 1

    student2 = Student("David", 20, 75)
    student3 = Student("Nancy", 21, 85)
    management.add_student(student2)
    management.add_student(student3)
    assert len(management.students) == 3

def test_search_student():
    management = StudentManagement()
    student1 = Student("John", 22, 55)
    student2 = Student("David", 20, 75)
    student3 = Student("Nancy", 21, 85)
    management.add_student(student1)
    management.add_student(student2)
    management.add_student(student3)
    result = management.search_student('John')
    assert len(result) > 0
    assert result[0].age == 22
    assert result[0].grade == 55

def test_remove_student():
    management = StudentManagement()
    student1 = Student("John", 22, 55)
    student2 = Student("David", 20, 75)
    student3 = Student("Nancy", 21, 85)
    management.add_student(student1)
    management.add_student(student2)
    management.add_student(student3)

    # found
    result = management.remove_student('John')
    # assert len(management.students) == 2
    assert result == "Student removed successfully."

    found_student = management.search_student('John')
    assert len(found_student) == 0

    # not found
    result = management.remove_student('Ben')
    # assert len(management.students) == 2
    assert result == "Student not found in the database."



