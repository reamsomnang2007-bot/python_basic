# collection = single "variable" use to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but add/remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

# collection
#fruit = "apple"

# list
# fruits = ["apple", "banana", "cherry", "orange"]
#print(fruit[0])
# shows all the functions you can use with lists
# print(dir(fruits)) 
# print(help(fruits))
# print(len(fruits))
# print("coconut" in fruits) print false because coconut is not in the list
# fruits[0] = "grape"
# fruits.append("grape") add grape to the end of the list
# fruits.remove("cherry") remove cherry from the list
# fruits.insert(0, "grape") add grape to the beginning of the list
# fruits.sort() sort elements in the list 
# fruits.reverse() reverse elements in the list 
# fruits.clear() clear all the elements in the list
# print(fruits.index("orange")) print the index of orange in the list
# print(fruits.count("apple"))

# sets
# fruits = {"apple", "banana", "cherry", "orange", "apple"}
# fruits.add("grape") add grape to the set
# fruits.remove("cherry")  remove cherry from the set
# fruits.clear() clear all the elements in the set
# fruits.pop() remove a random element from the set

# Tuples
fruits = ("apple", "banana", "cherry", "grape", "apple")
# print(help(fruits))
# print(fruits.index("apple"))
# print(fruits.count("apple"))

for fruit in fruits:
    print(fruit, end = " ")



