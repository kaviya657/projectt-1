import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits if use_digits else ""
    specials = string.punctuation if use_specials else ""

    all_chars = lower + upper + digits + specials
    if not all_chars:
        return "Error: No characters selected for password."

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# User Input
length = int(input("Enter password length: "))
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_specials = input("Include special characters? (y/n): ").lower() == 'y'

# Generate & Print Password
print("\nGenerated Password:", generate_password(length, use_digits, use_specials))

# User Input
length = int(input("Enter password length: "))
use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
use_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'

# Generate & Print Password
print("\nGenerated Password:", generate_password(length, use_digits, use_specials))

