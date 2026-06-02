# logical operators = evaluate multiple conditions (or, and , not)
#                     or = at least one condition must be True
#                     and = both condition must be True
#                     not = inverts the condition (not False or not True)

temp = int(input("Enter temperature: "))
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is Hot outside!")
    print("It is sunny!")
elif temp <= 0 and is_sunny:
    print("Ít is Cold outside!")
    print("It is sunny!")
elif temp < 28 and temp < 0 and is_sunny:
    print("It is Warm outside!")
    print("It is sunny!")
elif temp >= 28 and not is_sunny:
    print("It is not outside!")
    print("It is Cloudy!")
elif temp <= 0 and not is_sunny:
    print("It is Cold outside!")
    print("It is Cloudy!")