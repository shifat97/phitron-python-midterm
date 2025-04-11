# Task 1
class StudentDatabase:
    student_list = []

    def add_student(self, student):
        self.student_list.append(student)

class Student:
    # Task 2
    def __init__(self, student_id, name, department, is_enrolled):
        # Task 9
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
    
    # Get student id via getter
    def get_student_id(self):
        return self.__student_id
    
    # Task 4
    def enroll_student(self):
        # Task 8
        if self.__is_enrolled is not True:
            self.__is_enrolled = True
            print("\nEnrolled successfully")
        else:
            print("\nStudent already enrolled")
    
    # Task 5
    def drop_student(self):
        # Task 8
        if self.__is_enrolled is False:
            print("\nStudent is not enrolled yet!")
        else:
            self.__is_enrolled = False
            print("\nStudent dropped successfully")
    
    # Task 6
    def view_student_info(self):
        print()
        print("*********************")
        print(f"Student Id: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Is Enrolled: {self.__is_enrolled}")
        print("*********************")
        print()


# Task 3
john = Student(101, "John Doe", "CSE", False)
ghost = Student(102, "Simon Riley", "SWE", False)
zara = Student(103, "Zara Khan", "NFE", False)

student_db = StudentDatabase()

student_db.add_student(john)
student_db.add_student(ghost)
student_db.add_student(zara)


while True:
    # Task 7
    print()
    print("1. View All Student")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
    print()

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        for student in student_db.student_list:
            student.view_student_info()

    elif user_choice == 2:
        id = int(input("Enter student ID: "))
        found = False
        for student in student_db.student_list:
            if student.get_student_id() == id:
                found = True
                student.enroll_student()
        # Task 8
        if found is False:
            print("\nInvalid student id!")

    elif user_choice == 3:
        id = int(input("Enter student ID: "))
        found = False
        for student in student_db.student_list:
            if student.get_student_id() == id:
                found = True
                student.drop_student()
        # Task 8
        if found is False:
            print("\nInvalid Student id!")
    else:
        break