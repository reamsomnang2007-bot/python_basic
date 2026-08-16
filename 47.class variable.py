# class variable = shared among all instances of a class
#                  defind outside the constructor
#                  allow you to share data among all objects created for that class

class Student:

    class_year = 2025
    num_student = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1
    def print_student(self):
        print(f"My name is {self.name}. I'm {self.age} year olds!")
    
student1 = Student("Ream Somnang", 19)
student2 = Student("Im Mengchorng", 19)
student3 = Student("Meas Chandara", 19)
student4 = Student("Tal Davit", 19)
student1.print_student()
student2.print_student()
student3.print_student()
student4.print_student()
print(f"My graduating class of {Student.class_year} has {Student.num_student} student.")


class Emplyee:
    def __init__(self, name, gender, age, salary):
        self.name = name
        self.gender = gender
        self.age = age
        self.salary = salary
        
    def show_student(self):    
        print(f"Emplyee : {self.name} {self.gender} {self.age} {self.salary}")

e1 = Emplyee("Dara", "M", 25, 250)
e2 = Emplyee("Tola", "M", 27, 230)
e3 = Emplyee("Nona", "F", 23, 180)
e4 = Emplyee("Cheata", "F", 21, 210)
print("---------- Output ----------")
e1.show_student()
e2.show_student()
e3.show_student()
e4.show_student()
print("----------------------------")
