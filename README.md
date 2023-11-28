# 100 Days Of Code Python Pro Bootcamp

# Checklist
- [x] Day 1: Working With Variables in Python to Manage Data.
- [x] Day 2: Understanding Data Types And How To Manipulate Strings
- [x] Day 3: Control Flow And Logical Operators
- [x] Day 4: Randomisation and Python Lists
- [x] Day 5: Python Loops
- [x] Day 6: Functions & Karel
- [x] Day 7: Hangman
- [x] Day 8: Function Parameters and Caesar Cipher
- [x] Day 9: Dictionaries, Nesting
- [x] Day 10: Functions With Outputs
- [ ] Day 11: Blackjack Capstone Project
- [x] Day 12: Scope & Number Guessing Game
- [x] Day 13: Debugging

# Table of Contents

1. [Day 10: Functions With Outputs](#day-10-functions-with-inputs)
    - [Docstrings](#103-docstrings)
    - [Combining Dictionaries and Functions](#104-combining-dictionaries-and-functions)

# Day 10: Functions With Inputs

## 103: Docstrings
If we wan't to create documentation for the funcitons that we create we can use docstrings. 
Docstrings come straight after function declaration and we use `""" .. """` syntax.

I.e. 
```python
def sum(num1, num2):
    # docstring
    """sum is a function which takes two parameters - num1 and num2 - and returns the sum of both"""

    return num1 + num2
```

## 104: Combining Dictionaries and Functions.

### Storing functions in dictionaries
We can store functions in dictionaries in the following way:

```python
function_dictionary = {
    "key1": function_1,
    "key2": function_2,
}
```

In this form we can see that we don't use `()` or function parameters. We can access the functions in the same way that we have done previously:

```python
chosen_function = function_dictionary["key1"]

# Executing the function
chosen_function(parameter_1_of_function_1, parameter_2_of_function_1, ...)
```


