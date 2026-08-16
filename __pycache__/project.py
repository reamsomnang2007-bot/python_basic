class Student:
    def __init__(self, id = None, name = None, gender = None, age = None, course = None, classroom = None, contact = None):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.course = course
        self.classroom = classroom
        self.contact = contact

    def add_student(self):
        print("---------- Add Student -----------")
        self.id = int(input("ID: "))
        self.name = input("Name: ")
        self.gender = input("Gender: ")
        self.age = int(input("Age: "))
        self.course = input("Course: ")
        self.classroom = input("Classroom: ")
        self.contact = input("Contact: ")
        print("----------------------------------")

    def display(self):
        print(f"{self.id:<6}{self.name:<15}{self.gender:<10}{self.age:<8}{self.course:<15}{self.classroom:<15}{self.contact:<15}")

    def edit_student(self):
        print("---------- Option Edit ----------")
        print("[1]. Edit ID")
        print("[2]. Edit Name")
        print("[3]. Edit Gender")
        print("[4]. Edit Age")
        print("[5]. Edit Course")
        print("[6]. Edit Classroom")
        print("[7]. Edit Contact")
        print("----------------------------------")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("----- Edit ID -----")
            new_id = int(input("---> New ID: "))
            self.id = new_id
            print("\nEdit successfully...")
        elif choice == 2:
            print("----- Edit Name -----")
            new_name = input("---> New Name: ")
            self.name = new_name
            print("\nEdit successfully...")
        elif choice == 3:
            print("----- Edit Gender -----")
            new_gender = input("---> New Gender: ")
            self.gender = new_gender
            print("\nEdit successfully...")
        elif choice == 4:
            print("----- Edit Age -----")
            new_age = input("---> New Age: ")
            self.age = new_age
            print("\nEdit successfully...")
        elif choice == 5:
            print("----- Edit Course -----")
            new_course = input("---> New Course: ")
            self.course = new_course
            print("\nEdit successfully...")
        elif choice == 6:
            print("----- Edit Classroom -----")
            new_classroom = input("---> New Classroom: ")
            self.classroom = new_classroom
            print("\nEdit successfully...")
        elif choice == 7:
            print("----- Edit Contact -----")
            new_contact = input("---> New contact: ")
            self.contact = new_contact
            print("\nEdit successfully...")
        else:
            print("Invalid choice...!")


def menu():
    print("------------------------------------------------")
    print(">>>>>>> Student List Management System <<<<<<<<<")
    print("------------------------------------------------")
    print("[1]. Add Student")
    print("[2]. List All Student")
    print("[3]. Search Student")
    print("[4]. Edit Student")
    print("[5]. Delete Student")
    print("[6]. Exit Program")
    print("------------------------------------------------")
def search():
    print("[1]. Search by ID")
    print("[2]. Search by Name")

def edit():
    print("[1]. Edit by ID")
    print("[2]. Edit by Name")

def delete():
    print("[1]. Delete by ID")
    print("[2]. Delete by Name")

def header():
    print(f"{"ID":<6}{"Name":<15}{"Gender":<10}{"Age":<8}{"Course":<15}{"Classroom":<15}{"Contact":<15}")

student_list = []
while True:
    menu()
    new_student = Student()
    choice = int(input("YOUR CHOICE: "))
    match choice:
        case 1:
            new_student.add_student()
            duplicate = False
            for s in student_list:
                if s.id == new_student.id:
                    duplicate = True
                    break
            if duplicate:
                print("\nA Student with this is already exist!")
            else:
                student_list.append(new_student)
                print("\nAdd Student Successfully...")

        case 2:
            print("-------------------------------- List All Student ---------------------------------")
            if not student_list:
                print("Not student found in the system....!")
            else:
                header()
                for s in student_list:
                    s.display()
                print("--------------------------------------------------------------------------------")
        case 3:
            print("---------- Search Student ----------")
            search()
            print("------------------------------------")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("-------- Search by ID ----------")
                sId = int(input("Enter ID to search: "))
                found = False
                
                for student in student_list:
                    if student.id == sId:
                        header()
                        student.display()
                        found = True 
                        break
                if not found:
                    print(f">>>> {sId} is not found.")
            elif choice == 2:
                print("-------- Search by Name ----------")
                sName = input("Enter Name to search: ")
                found = False
                for student in student_list:
                    if student.name == sName:
                        header()
                        student.display()
                        found = True
                if not found:
                    print(f">>>> {sName} is not found...!")
            else:
                print("Invalid choice!")
        case 4:
            print("---------- Edit Student ----------")
            edit()
            print("----------------------------------")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("-------- Edit by ID ----------")
                sId = int(input("Enter ID to Edit: "))
                found = False
                for student in student_list:
                    if student.id == sId:
                        header()
                        student.display()
                        student.edit_student()
                        found = True 
                        break
                if not found:
                    print(f">>>> {sId} is not found.")
            elif choice == 2:
                print("-------- Edit by Name ----------")
                sName = input("Enter Name to Edit: ")
                found = False
                for student in student_list:
                    if student.name == sName:
                        header()
                        student.display()
                        student.edit_student()
                        found = True
                if not found:
                    print(f">>>> {sName} is not found...!")
            else:
                print("Invalid choice!")
        case 5:
            print("---------- Delete Student ----------")
            delete()
            print("------------------------------------")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("-------- Delete by ID ----------")
                sId = int(input("Enter ID to Delete: "))
                found = False              
                for student in student_list:
                    if student.id == sId:
                        student_list.remove(student)
                        print(f"Student ID: {sId} was delete...!")
                        found = True 
                        break
                if not found:
                    print(f">>>> {sId} is not found.")
            elif choice == 2:
                print("-------- Delete by Name ----------")
                sName = input("Enter Name to Delete: ")
                found = False
                for student in student_list:
                    if student.name == sName:
                        student_list.remove(student)
                        print(f"Student Name: {sName} was delete...!")
                        found = True
                if not found:
                    print(f">>>> {sName} is not found...!")
            else:
                print("Invalid choice!")
        case 6:
            print("Thanks for visiting...!")
            break
        case _:
            print("That is not valid chocie!")