import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator.")



letters_amount = int(input("How many letters would you like your password to have?"))
numbers_amount = int(input("How many numbers would you like your password to have?"))
symbols_amount = int(input("How many symbols would you like your password to have?"))

#1
password_one = ""
total_characters = letters_amount + numbers_amount + symbols_amount
max_letters = 0
max_numbers = 0
max_symbols = 0

while len(password_one) != total_characters:
    random_list = random.randint(0, 2)

    if random_list == 0 and max_letters != letters_amount:
        password_one += random.choice(letters)
        max_letters += 1
    elif random_list == 1 and max_numbers != numbers_amount:
        password_one += random.choice(numbers)
        max_numbers += 1
    elif random_list == 2 and max_symbols != symbols_amount:
        password_one += random.choice(symbols)
        max_symbols += 1

print(password_one)

#2
random_characters = []

for i in range(0, numbers_amount):
    random_characters.append(random.choice(numbers))

for i in range(0, letters_amount):
    random_characters.append(random.choice(letters))

for i in range(0, symbols_amount):
    random_characters.append(random.choice(symbols))

password_two = ""

for i in range(0, len(random_characters)):
    random_character = random.choice(random_characters)
    password_two += random_character
    random_characters.remove(random_character)

print(password_two)


#3
random_characters = []

for i in range(0, numbers_amount):
    random_characters.append(random.choice(numbers))

for i in range(0, letters_amount):
    random_characters.append(random.choice(letters))

for i in range(0, symbols_amount):
    random_characters.append(random.choice(symbols))

random.shuffle(random_characters)
password_three = ""

for random_character in random_characters:
    password_three += random_character


print(password_three)