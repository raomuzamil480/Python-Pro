import string
import random

chars = list(string.punctuation + string.ascii_letters + string.digits)

key = chars.copy()
random.shuffle(key)

# Encrypt
plain_text = input("Enter message to encrypt: ")
cipher = ""

for letter in plain_text:
    if letter in chars:
        index = chars.index(letter)
        cipher += key[index]
    else:
        cipher += letter

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher}")

print()

# Decrypt
cipher = input("Enter encrypted message: ")
plain_text = ""

for letter in cipher:
    if letter in key:
        index = key.index(letter)
        plain_text += chars[index]
    else:
        plain_text += letter

print(f"Encrypted message: {cipher}")
print(f"Original message: {plain_text}")