import random
import string

def generate_password(length):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure at least one character from each set is included
    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)
    password += random.choice(special_characters)

    # Generate the remaining characters randomly
    for _ in range(length - 4):
        password += random.choice(all_characters)

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    num_passwords = int(input("How many passwords do you want to generate? "))
    min_length = 5
    passwords = []

    print("\nGenerating Passwords:")
    for i in range(num_passwords):
        length = int(input(f"Enter the length of password {i + 1} (minimum {min_length}): "))
        if length < min_length:
            print(f"Password length should be at least {min_length}. Using default length.")
            length = min_length

        password = generate_password(length)
        passwords.append(password)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"{i}. {password}")
