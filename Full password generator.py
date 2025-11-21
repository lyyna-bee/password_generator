import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") #see how you should enter BOTH upper and lowercase
numbers = list("0123456789")
symbols = list("!@#$%^&*()-_=+[]{};:,.<>?/")

# Ask for password length
while True:
    try:
        password_length = int(input("Enter the password length (must be at least 8): "))
        if password_length < 8:
            print("❌ Password length must be at least 8. Try again!")
        else:
            break
    except ValueError:
        print("❌ Please enter a valid number!")

# Ask how many passwords to generate
while True:
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        if num_passwords < 1:
            print("❌ Please enter at least 1.")
        else:
            break
    except ValueError:
        print("❌ Please enter a valid number!")

# Generate multiple passwords
print("\nHere are your passwords:")
for i in range(num_passwords):
    # Split the length across letters, numbers, and symbols
    nr_letters = random.randint(1, password_length - 2)
    nr_numbers = random.randint(1, password_length - nr_letters - 1)
    nr_symbols = password_length - nr_letters - nr_numbers

    # Pick random characters
    password_letters = random.choices(letters, k=nr_letters)
    password_numbers = random.choices(numbers, k=nr_numbers)
    password_symbols = random.choices(symbols, k=nr_symbols)

    # Combine and shuffle
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"{i+1}: {password}")