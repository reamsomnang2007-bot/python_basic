# args      = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#             * unpacking operator
#           1. positional   2. default  3.keyword   4. arbitrary

# *args explain
def add(*args):
    print(type(args))
add()

#   total = 0
#    for arg in args:
#        total += arg
#    print(total)

# dd(1, 2, 3, 4)
def display_name(*names):
    for name in names:
        print(name, end=" ")

display_name("Mr.","Ream", "Somnang", "Professortional")


# **kwargs explain
def print_address(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}: {values}")
print_address(street = "Street 2004",

              city = "Phnom Penh",
              middle_of_country = "Kompong Thom",
              code= "+855")

def shipping_lable(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()

    print(f"{kwargs.get('street')} ")
    print(f"{kwargs.get('apt')}")
    if 'city' in kwargs:
        print(f"{kwargs.get('city')} and {kwargs.get('zip')}")
    else:
        print(f"zip: {kwargs.get('zip')}")

shipping_lable("Mr", "Ream", "Somnang", "Software Developer",
               street = "Street 2004",
               apt = "501",
               city = "Phnom Penh",
               zip = "+855"
               )

