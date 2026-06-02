# variable = a container for a values ( string, integer, float, boolean )
#            a variable behaves as if it was the value it contains
# Strings
first_name = "Ream"
last_name = "Somnang"
email = "reamsomnang2007@gmail.com"
print("---------- Strings ----------")
print(f"Hello, My name is {first_name} {last_name}")
print(f"Email: {email}")

# Integers
age = 19
quantity = 10
num_of_student = 69
print("---------- Integers ----------")
print(f"You are {age} years old!")
print(f"You are buying {quantity} items")
print(f"You class have {num_of_student} students!")

# Float
price = 19.99
gpa = 3.2
distance = 5.6
print("---------- Float ----------")
print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} km")

# Boolean ( True or False )
is_student = True
for_sale = False
is_online = True
print("---------- Boolean ----------")
if is_student:
    print("You are a student!")
else:
    print("You are not a student!")
if for_sale:
    print("That item is for sale!")
else:
    print("That item is not available!")
if is_online:
    print("You are online!")
else:
    print("You are offline!")