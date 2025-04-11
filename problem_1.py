class StudentDatabase:
    student_list = []

    def add_student(self, student):
        self.student_list.append(student)

class Student:
    def __init__(self, name, roll_no, gender):
        self.name = name
        self.roll_no = roll_no
        self.gender = gender
    
    def print_student(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Gender: {self.gender}")
        print("*********************")

john = Student("John Doe", 1, "Male")
ghost = Student("Simon Riley", 2, "Male")
zara = Student("Zara Khan", 3, "Female")

student_db = StudentDatabase()

student_db.add_student(john)
student_db.add_student(ghost)
student_db.add_student(zara)

for student in student_db.student_list:
    student.print_student()