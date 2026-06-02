# iterables = an object/collection that can return its elements one at a time
#            allowing it to be iterated over in a loop

# fruits = {"apple", "banana", "grapes", "pear"}
# for fruit in reversed(fruits):
#    print(fruit)

my_dictionary = {"a": 1, "b": 2, "c": 3}
for key, values in my_dictionary.items():
    print(f"{key} = {values}")
