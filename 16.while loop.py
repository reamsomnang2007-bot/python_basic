# while loop = execute some code WHILE some condition remains true

# example1
# age = int(input("Enter your age: "))
# while age < 0:
#    print("Age can't be negative!")
#    age = int(input("Enter your age: "))

# print(f"You are {age} year olds!")

# example2
# food = input("Enter a food you like (q to quit): ")
# while not food == 'q':
#    print(f"You like {food} !")
#    food = input("Enter a food you like (q to quit): ")
# print("Thank you for visiting...!")

# example3
num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a # between 1 - 10: "))
print(f"Your number is {num}")





