# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# for x in range(1, 11):
#     print(x)
# for x in reversed(range(1, 11)):
#     print(x)
# for y in range(1, 11, 2):
#    print(y)
credit_card = "123-456-789-987-654-321"
for x in credit_card:
    print(x)
name = input("Enter your name to count: ")
for x in name:
    print(x)
for x in range(1, 21):
    if x == 13:
        continue
    elif x == 18:
        break
    else:
        print(x)



