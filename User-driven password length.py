import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ask for password length (random)
while True:
    try:
        password_length = int(input("Enter the maximum password length (must be at least 8):\n"))

        if password_length < 8:
            print("Password must be at least 8!")
        else:
            break

    except ValueError:
        print("Please enter a valid number!")

# ask how many passwords to generate

while True:
    try:
        num_passwords = int(input("How many passwords would you like to generate (at least 1)?\n"))
        if num_passwords < 1:
            print("Please enter at least 1.")
        else:
            break
    except ValueError:
        print("Please enter a valid number!")

#generate multiple passwords

print("Here are your passwords:\n")
for i in range(num_passwords):
        nr_letters = random.randint(1, password_length -2)
        nr_numbers = random.randint(1,password_length -1)
        nr_symbols = password_length - nr_numbers - nr_letters

        password_letters = random.choices(letters, k=nr_letters)
        password_numbers = random.choices(numbers, k=nr_numbers)
        password_symbols = random.choices(symbols, k=nr_symbols)

        password_list = password_symbols + password_numbers + password_letters
        random.shuffle(password_list)

        password = "".join(password_list)
        print(f"{i+1}: {password}")



