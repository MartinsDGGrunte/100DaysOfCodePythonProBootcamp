# 1. in try block try to do something that might cause an error
# 2. Catch Exceptions
# 3. Read the file after the exception was caught
# 4. Finally close the file

try:
    file = open("some_file.txt")
    dictionary = {
        "key": "value"
    }
    print(dictionary["key"])
except FileNotFoundError:
    file = open("some_file.txt", "w")
    file.write("Something")
except KeyError as key_error:
    print(f"There is no key: {key_error}\n")
else:
    print(file.read())
finally:
    file.close()
    print("File was closed.")
