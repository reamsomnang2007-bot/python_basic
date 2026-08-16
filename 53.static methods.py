# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions
# Instance methods = Best for operations on instances of the class (objects)
# Stactic methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Software Engineering", "Admin", "Account", "IT support"]
        return position in valid_position
    
em1 = Employee("Ream Somnang", "Software Engineering")
em2 = Employee("Dara", "Admin")
em3 = Employee("Menghour", "Account")
em4 = Employee("Mengchorng", "IT support")
    
print(Employee.is_valid_position("Software Engineering"))
print(Employee.is_valid_position("Web developer"))
print(em1.get_info())
print(em2.get_info())
print(em3.get_info())
print(em4.get_info())