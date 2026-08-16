# Decorator = A function that extends the behavior of another function
#             w/o meditying the base function 
#             Pass the base function as an argument to the decorator

def add_sprinkless(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles!")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge!")
        func(*args, **kwargs)
    return wrapper

@add_sprinkless
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨!")

get_ice_cream("vanilla")

def decorator(func):
    def wrapper():
        print("Befor calling the function")
        func()
        print("After calling the function")
    return wrapper
@decorator
def greet():
    print("Hello, World!")
greet()

def decorator_name(function):
    def dd(*args, **kwargs):
        print("Befor execution")
        function(*args, **kwargs)
        print("After execution")
    return dd

def decorator_age(function):
    def dd(*args, **kwargs):
        print("Before execution")
        function(*args, **kwargs)
        print("After execution")
    return dd

@decorator_age
@decorator_name

def add(a, b):
    print(f"a + b = {a + b}")

add(4, 6)