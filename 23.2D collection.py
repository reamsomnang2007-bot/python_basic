# fruits = ["apple", "banana", "cherry"]
# vegetables = ["celery", "carrot", "salad"]
# meats = ["chicken", "beef", "fish"]
# groceries = [fruits, vegetables, meats]

# or like this it same  
# groceries = [["apple", "banana", "cherry"],
#              ["celery", "carrot", "salad"], 
#              ["chicken", "beef", "fish"]]           


# for collection in groceries:
#    for food in collection:
#        print(food, end= " ")
#    print()

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for item in row:
        print(item, end=" ")
    print()

