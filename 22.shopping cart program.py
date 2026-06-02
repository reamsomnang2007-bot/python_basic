foods = []
prices = []
total = 0

while True:
    food = input("Enter a food item (or 'done' to finish): ")
    if food == "done":
        break
    else:
        price = float(input("Enter the price of the food item: $ "))
        foods.append(food)
        prices.append(price)
        total += price
print("===== Shopping Cart =====")
for food in foods:
    print(food, end=" ")
print(f"\nYour total is: ${total:.2f}")