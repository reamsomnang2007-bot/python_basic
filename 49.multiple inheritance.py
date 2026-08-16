# multiple inheritance = inherit from more the one parent class C(A, B)
# mulilevel inheritance = inherit for a parent which inherits fron another parent C(B) <- B(A) <- A
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("KOKO")
rabbit.eat()
fish = Fish("NONO")
fish.sleep()