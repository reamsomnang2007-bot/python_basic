def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

def verity(index):
    if not index:
        print("The number is not found in the list")
    else:
        print("The number is found in the index : ", index)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 10)
verity(result)