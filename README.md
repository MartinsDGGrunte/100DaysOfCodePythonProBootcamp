# 100 Days Of Code Python Pro Bootcamp

# Checklist
***Beginner***
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
- [x] Day 14: Higher - Lower Game Project

***Intermediate***
- [x] Day 15: Local Development Environment Setup & Coffee Machine
- [ ] Day 16: Object-Oriented Programming



# Table of Contents

1. [Day 10: Functions With Outputs](#day-10-functions-with-inputs)
    - [Docstrings](#103-docstrings)
    - [Combining Dictionaries and Functions](#104-combining-dictionaries-and-functions)
2. [Day 16: Object-Oriented Programming (OOP)](#day-16-object-oriented-programming-oop)
    - [Why do we need OOP?](#146-why-do-we-need-oop)

# Day 10: Functions With Inputs

## 103: Docstrings
If we want to create documentation for the functions that we create we can use docstrings. 
Docstrings come straight after function declaration and we use `""" .. """` syntax.

I.e. 
```python
def some_sum(num1, num2):
    # docstring
    """sum is a function which takes two parameters - num1 and num2 - and returns the sum of both"""

    return num1 + num2
```

## 104: Combining Dictionaries and Functions.

### Storing functions in dictionaries
We can store functions in dictionaries in the following way:

```python
def function_1():
   pass

def function_2():
   pass

function_dictionary = {
    "key1": function_1,
    "key2": function_2,
}
```

In this form we can see that we don't use `()` or function parameters. We can access the functions in the same way that we have done previously:

```python
def function_1():
   pass

def function_2():
   pass

function_dictionary = {
    "key1": function_1,
    "key2": function_2,
}

chosen_function = function_dictionary["key1"]

# Executing the function
chosen_function()
```

# Day 16: Object-Oriented Programming (OOP)

## 146: Why do we need OOP
1. OOP can be used for dividing a more complex task into smaller portions that can be resolved by different teams
2. OOP improves the efficiency of the program development compared to Spaghetti-Like ***Procedural Programming***
3. In case of OOP we can make the code more reusable, in case we wanted to create a similar project in the future.
4. OOP is modelled in a way that we create classes (roles, partners, stakeholders) which contain *attributes* and *methods*.
   * *attributes* are properties that this class has. (what do we have?)
   * *methods* are functions that represent what this role can do. (what can we do?)

