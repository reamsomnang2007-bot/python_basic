# Inheritance = Allow a class to inherit attributes and methoda from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.isalive = True
    
    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Car(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")

dog = Dog("Scooby")
car = Car("Garfield")
mouse = Mouse("Mickey")

print(dog.name, dog.isalive)
dog.eat()
dog.sleep()
dog.speak()
print(car.name)
print(mouse.name)
car.speak()
