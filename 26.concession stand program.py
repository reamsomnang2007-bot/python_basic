# Concession stand program
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 2.50,
        "fries": 3.50, 
        "soda": 1.75,
        "candy": 1.25,
        "lemonade": 4.25,
        "hot dog": 3.75,
        "ice cream": 2.75,}
cart = []
total = 0
print("========== Menu ==========")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("==========================")
while True:
    item = input("Enter a menu item to add to your cart (q to quit): ").lower()
    if item == "q":
        break
    elif menu.get(item) is not None:
         cart.append(item)
         total += menu.get(item)
print("========== Your Order ==========")
for item in cart:
    print(f"{item}", end= " ")
print(f"\nTotal: ${total:.2f}")


