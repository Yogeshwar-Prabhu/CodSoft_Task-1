import random
import string

def generate_password():
    try:
        length = int(input("Enter password length: "))
        if length < 4:
            print("Password should be at least 4 characters long!")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a number!")

generate_password()