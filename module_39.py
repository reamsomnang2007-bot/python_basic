# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# print(help("modules")) show all modules
# print(help("math"))

# import math
# # import math as m
# # from math import pi
# a, b, c, d = 1, 2, 3, 4
# print(math.pi ** a)
# print(math.pi ** b)
# print(math.pi ** c)
# print(math.pi ** d)

# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)

pi = 3.1159

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius 

def area(radius):
    return pi * radius ** 2

