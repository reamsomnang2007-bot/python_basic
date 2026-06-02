# format specifiers = {value:flags} format a value based on what
#                     flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma seperator


price1 = 3.14159
price2 = -343.2221
price3 = 12.56
price4 = 12000000000.34

print(f"Price1 is: ${price1:.2f}")
print(f"Price1 is: ${price1:<10}")
print(f"Price1 is: ${price1:>10}")
print(f"Price1 is: ${price1:^10}")
print(f"Price2 is: ${price2:10.3f}")
print(f"Price2 is: ${price2:,}")
print(f"Price3 is: ${price3:+}")
print(f"Price3 is: ${price3: ,.2f}")
print(f"Price4 is: ${price4:+,}")

