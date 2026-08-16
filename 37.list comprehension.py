# list comprehension = a concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * 4 for z in range(1, 11)]
# print(squares)

# fruits = ["apple", "banana", "orange", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6]
# positive_num = [num for num in numbers if num >= 0]
# negative_num = [num for num in numbers if num < 0]
# even_num = [num for num in numbers if num % 2 == 0]
# odd_num = [num for num in numbers  if not num % 2 == 0]
# print(odd_num)

grades = [85, 42, 79, 90, 45, 65]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
