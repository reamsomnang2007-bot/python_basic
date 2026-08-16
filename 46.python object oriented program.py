# object = a "bundle" of relates attributes (variables) and methods (function)
# example: phone, cup, book
# class = (blueprint) used to design the structrue and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}.")
    def stop(self):
        print(f"You stop the {self.color} {self.model}.")
    
    def print_car(self):
        print(f"{self.model} {self.year} {self.color} {self.for_sale}")


car1 = Car("BMW", 2025, "Green", True)
car2 = Car("Audi", 2026, "White", False)
car1.print_car()
car1.drive()
car1.stop()
car2.print_car()


        