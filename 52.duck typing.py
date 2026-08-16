# "Dack typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimun necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True 

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("Meov!")

class Car(Animal):
    alive = False
    def speak(self):
        print("Car is driving!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
