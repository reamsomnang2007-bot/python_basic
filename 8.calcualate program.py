# Python calculator
operator = input("Enter an operator ( + - * / ) : ")
num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))

if operator == "+":
    result = num1 + num2
    print(f"Result: {round(result, 3)}")
elif operator == "+":
    result = num1 - num2
    print(f"Result: {round(result, 3)}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {round(result, 3)}")
elif operator == "/":
    if num2 == 0:
        print("Undefined")
    else:
        result = num1 / num2
        print(f"Result: {round(result, 3)}")
else:
    print(f"{operator} is not valid operator!")
