# Membership operator = used to test whether a value or variable is found in a squence
#                       string , list, tuple, set, or dictionary
#                       1. in
#                       2. not in

# word = "SOMNANG"
# letter = input("Guess a letter in the secret word: ")
# if letter in word:
#     print(f"There is {letter}")
# else:
#     print(f"{letter} was not found.")
# or 
# if letter not in word:
#     print(f"{letter} was not found.")
# else:
#     print(f"There is {letter}")

# students = {"Somnang", "Dara", "Chorng"}

# student = input("Enter the name of a student: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} is not a student")

# grades = {"Somnang": "A",
#           "Kosin": "B", 
#           "Sola": "A"}
# student = input("Enter the name of a student: ")
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "reamsomnang2007@gmail.com"

if "@" in email and "." in email:
    print("Valid email...")
else:
    print("Invalid email!")




