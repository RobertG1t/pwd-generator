import os
import random
import string

def generate_password(length, complexity):
    """Generate a random password of specified length and complexity."""
    chars = ''
    if 'l' in complexity:
        chars += string.ascii_lowercase
    if 'u' in complexity:
        chars += string.ascii_uppercase
    if 'd' in complexity:
        chars += string.digits
    if 's' in complexity:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

print("Password complexity options:")
print("  l: Lowercase letters")
print("  u: Uppercase letters")
print("  d: Digits")
print("  s: Symbols")

length = int(input("Enter password length: "))
complexity = input("Enter password complexity (e.g. 'lu' for lowercase and uppercase letters): ")

password = generate_password(length, complexity)
print("Generated password: ", password)

filename = 'passwords.txt'
with open(filename, 'a') as f:
    f.write(password + '\n')

print(f"Password saved in {os.path.abspath(filename)}")
