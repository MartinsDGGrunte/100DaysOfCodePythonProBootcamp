# Addition Function
def add(n1, n2):
    """Function which adds two numbers together"""
    return n1 + n2

# Subtraction Function
def subtract(n1, n2):
    """Function which subtracts n1 from n2"""
    return n1 - n2

# Multiplication Function
def multiply(n1, n2):
    """Function which multiplies two numbers n1 and n2"""
    return n1 * n2

# Division Function
def divide(n1, n2):
    """Function which divides n1 by n2"""
    return n1 / n2

# Dictionary which stores the functions
function_dictionary = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

user_choice = "y"
first_time = True
while user_choice == "y":

    # Calculator Main Code:
    if first_time:
        num1 = int(input("What's the first number?: "))
        first_time = False
    else:
        num1 = answer

    for symbol in function_dictionary:
        print(symbol)
    chosen_function = input("Pick function from the list above: ")
    num2 = int(input("What's the second number?: "))

    if chosen_function in list(function_dictionary.keys()):
        answer = function_dictionary[chosen_function](num1, num2)
        print(f'{num1} {chosen_function} {num2} = {answer}')
    else:
        print("ERROR: Unsupported function provided.")
    
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if choice == 'n':
        break


