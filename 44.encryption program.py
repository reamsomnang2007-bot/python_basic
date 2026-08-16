import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
str_punctuation = string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
str_digits = string.digits # 0123456789
str_ascii_letters = string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(str_punctuation)
print(str_digits)
print(str_ascii_letters)

random.shuffle(key)
# print(f"chars: {chars}")
# print(f"key: {key}")

# encrypt

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# ENCRYPT

cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")

