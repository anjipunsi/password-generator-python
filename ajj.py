import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.ascii_uppercase 
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a password of default length 12
password = generate_password()
print("Generated Password:", password)