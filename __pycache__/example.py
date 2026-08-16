import random
import string

length = int(input("Password length: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

password = []

# Ensure at least one of each
password.append(random.choice(letters))
password.append(random.choice(digits))
password.append(random.choice(symbols))

# Fill the rest
all_chars = letters + digits + symbols
for _ in range(length - 3):
    password.append(random.choice(all_chars))

# Shuffle so pattern is not predictable
random.shuffle(password)

print("Generated password:", ''.join(password)
