# keyword arguments = an argument preceded by an identifier help with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. keyword 4. arbitrary

# def hello(greeting, tittle, first, last):
#    print(f"{greeting} {tittle}{first}{last}")

# hello("Hello", tittle= "Mr.", first="Ream", last=" Somnang")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=855, area=972, first=264, last=786)
print(phone_num)