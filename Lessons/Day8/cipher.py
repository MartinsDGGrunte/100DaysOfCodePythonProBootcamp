import string
letters = list(string.ascii_lowercase)
message_indexes = []

def main():
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    process(method=choice)

def process(method):
    
    shifted_indexes = []
    original_message = input("Type your message:\n")
    shift_number = int(input("Type your shift number:\n"))

    for letter in original_message:
        if method == "encode":
            letter_index = letters.index(letter) + shift_number
            if letter_index > 25:
                letter_index = letter_index - (len(letters) - 1)
                shifted_indexes.append(letter_index)
            else:
                shifted_indexes.append(letter_index)
        elif method == "decode":
            letter_index = letters.index(letter) - shift_number
            if letter_index < 0:
                letter_index = letter_index + (len(letters) - 1)
                shifted_indexes.append(letter_index)
            else:
                shifted_indexes.append(letter_index)
    
    return_message = ""
    for index in shifted_indexes:
        return_message += letters[index]
    
    if method == "encode":
        print(f"Here's the encoded result: {return_message}")
    elif method == "decode":
        print(f"Here's the decoded result: {return_message}")
    
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if repeat == "yes":
        main()

main()