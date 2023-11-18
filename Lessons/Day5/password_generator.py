import random, string

# List of English language letters
letters = list(string.ascii_letters)

# List of numbers
numbers = list(string.digits)

# List of keyboard symbols
symbols = list(string.punctuation)

num_of_letters = int(input("How many letters would you like in your password? "))
num_of_numbers = int(input("How many numbers would you like? "))
num_of_symbols = int(input("How many symbols would you like? "))

random_letter_indexes = []
for turns in range(1, num_of_letters):
    random_number = random.randint(0, len(letters))
    random_letter_indexes.append(random_number)

random_number_indexes = []
for turns in range(1, num_of_numbers):
    random_number = random.randint(0, len(numbers))
    random_number_indexes.append(random_number)

random_symbols_indexes = []
for turns in range(1, num_of_symbols):
    random_symbol = random.randint(0, len(symbols))
    random_symbols_indexes.append(random_symbol)

random_letters_string = ""
for index in random_letter_indexes:
    char = letters[index-1]
    random_letters_string += char
#print(random_letters_string)

random_numbers_string = ""
for index in random_number_indexes:
    char = numbers[index-1]
    random_numbers_string += char
#print(random_numbers_string)

random_symbols_string = ""
for index in random_symbols_indexes:
    char = symbols[index-1]
    random_symbols_string += char
#print(random_symbols_string)

combined_string = random_letters_string + random_numbers_string + random_symbols_string
combined_list = list(combined_string)
random.shuffle(combined_list)
generated_password = ''.join(combined_list)
print(f'Here is your password: {generated_password}')

