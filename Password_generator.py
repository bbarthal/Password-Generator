# Password Generator - Oasis Infobyte Internship

import random
import string

def generate_password():
    print("=== Random Password Generator ===")

    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password length should be at least 4.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("Generated Password:", password)
    
    except ValueError:
        print("Please enter a valid number.")

# Run the function
generate_password()
