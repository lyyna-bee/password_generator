import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_length = random.randint(8, 20)

nr_letters = random.randint( 1, password_length -2)
nr_numbers = random.randint(1, password_length - nr_letters - 1)
nr_symbols = password_length - nr_numbers - nr_letters

password_letters = random.sample(letters, k=nr_letters)
password_symbols = random.sample(symbols, k=nr_symbols)
password_numbers = random.sample(numbers, k=nr_numbers)

password_list = password_symbols + password_numbers +password_letters
random.shuffle(password_list)

password = "".join(password_list)

print("Your random password is: " + password)
