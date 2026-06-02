# nested loop = a loop within another loop (outer, inner)
#               outer loop:
#                   inner loop
# for x in range(3):
#    for y in range(1, 10):
#        print(y, end="")
#    print()

rows = input("Enter the number of rows: ")
columns = input("Enter the number of columns: ")
symbol = input("Enter a symbol to use: ")
for i in range(int(rows)):
    for j in range(int(columns)):
        print(symbol, end = "")
    print()