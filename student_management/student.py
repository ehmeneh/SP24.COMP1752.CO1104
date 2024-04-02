class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        print("Student object has been initialized.")

    def is_passing(self):
        # student passes if his/her grade > 40
        if self.grade > 40:
            return True
        else:
            return False



