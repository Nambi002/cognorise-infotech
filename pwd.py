import random
import string
import numpy as np

def generate_password(length):
    """
    Generate a random password of the specified length.
    The password includes uppercase letters, lowercase letters, digits, and special characters.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")

    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one character from each pool
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        # Prompt the user for the password length
        length = int(input("Enter the desired password length (minimum 4): "))

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
