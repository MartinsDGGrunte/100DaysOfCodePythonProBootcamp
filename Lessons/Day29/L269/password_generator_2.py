import random
import string


def generate_password():
    # List of English language letters
    letters = list(string.ascii_letters)

    # List of numbers
    numbers = list(string.digits)

    # List of keyboard symbols
    symbols = list(string.punctuation)

    password = ""
    for letter in range(1, 9):
        char = random.choice(letters)
        password += char

    for number in range(1, 6):
        c_number = random.choice(numbers)
        password += c_number

    for symbol in range(1, 4):
        c_symbol = random.choice(symbols)
        password += c_symbol

    password_mix = list(password)
    random.shuffle(password_mix)
    generated_password = ''.join(password_mix)
    return generated_password
