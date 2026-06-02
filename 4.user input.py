# input() = a function that prompts the user to enter data returns the entered data as a string
# name = input("What is your name?: ")
# age = input("How old are you?: ")
# age = int(age)
# age = age + 1
# print(f"Hello {name}!")
# print("HAPPY BIRTHDAY!")
# print(f"You are {age} years old!")
# Exercise 1
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is: {area} cm²")

# Exercise 2 Shopping card program
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: {total} $")