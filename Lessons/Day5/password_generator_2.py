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

password = ""
for letter in range(1, num_of_letters+1):
    char = random.choice(letters)
    password += char

for number in range(1, num_of_numbers + 1):
    c_number = random.choice(numbers)
    password += c_number

for symbol in range(1, num_of_symbols+1):
    c_symbol = random.choice(symbols)
    password += c_symbol

password_mix = list(password)
random.shuffle(password_mix)
generated_password = ''.join(password_mix)
print(f'Here is your password: {generated_password}')