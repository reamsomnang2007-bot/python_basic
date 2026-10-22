from pip._internal import self_outdated_check


class Student:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.age = 0
        self.gender = ""
        self.course = ""
        self.classroom = ""
        self.contact = ""

    def addStudent(self):
        self.id = int(input("ID : "))
        self.name = input("Name : ")
        self.age = int(input("Age : "))
        self.gender = input("Gender : ")
        self.course = input("Course : ")
        self.classroom = input("Classroom : ")
        self.contact = input("Contact : ")

    def printStudent(self):
        print(f"ID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Course : {self.course}")
        print(f"Classroom : {self.classroom}")
        print(f"Contact : {self.contact}")

def menu():
    print("==========[ Student System Management ]==========")
    print("[1]. Add Student")
    print("[2]. Display Students")
    print("=================================================")

students = []
while(True):
    menu()
    choice = int(input("Enter your choice : "))
    match(choice):
        case 1:
            print("=====[ Add Student ]=====")
            student = Student()
            student.addStudent()
            students.append(student)
            print("=========================")
        case 2:
            print("=====[ Display Students ]=====")
            for student in students:
                student.printStudent()
            print("==============================")



