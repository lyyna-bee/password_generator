import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(5, 9)
nr_symbols = random.randint(2, 5)
nr_numbers = random.randint(1, 4)

password_letters = random.choices(letters, k=nr_letters)
password_symbols = random.choices(symbols, k=nr_symbols)
password_numbers = random.choices(numbers, k=nr_numbers)

password_list = password_numbers + password_letters + password_symbols
random.shuffle(password_list)

password = "".join(password_list)
print("Your password is:", password)



