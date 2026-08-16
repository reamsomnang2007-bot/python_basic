# Class methods = Allow operation related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of student: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Ream Somnang", 3.8)
student2 = Student("Ream Somnang", 3.8)
student3 = Student("Ream Somnang", 3.8)
student4 = Student("Ream Somnang", 3.8)

print(Student.get_count())
print(Student.get_average_gpa())
