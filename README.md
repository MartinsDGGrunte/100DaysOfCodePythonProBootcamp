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
- [x] Day 16: Object-Oriented Programming
- [x] Day 17: Benefits of OOP
- [ ] Day 19: Instances, State and Higher Order Functions
- [x] Day 25: Working with CSV Data and the Pandas library
- [x] Day 26: List Comprehension and the NATO alphabet
- [x] Day 27: Tkinter *args, **kwargs and creating GUI programs
- [x] Day 28: Tkinter, Dynamic Typing and the Pomodoro Clock



# Table of Contents

1. [Day 10: Functions With Outputs](#day-10-functions-with-inputs)
    - [Docstrings](#103-docstrings)
    - [Combining Dictionaries and Functions](#104-combining-dictionaries-and-functions)
2. [Day 16: Object-Oriented Programming (OOP)](#day-16-object-oriented-programming-oop)
    - [Why do we need OOP?](#146-why-do-we-need-oop)
3. [Day 25: Working with CSV Data and the Pandas Library](#day-25-working-with-csv-data-and-the-pandas-library)
    - [Reading CSV Data in Python](#228-reading-csv-data-in-python)
      - [Opening Files in Python](#opening-files-in-python)
    - [DataFrames & Series: Working With Rows & Columns](#229-dataframes--series-working-with-rows--columns)
4. [Day 26: List Comprehension](#day-26-list-comprehension)
    - [How to create lists using List Comprehension](#235-how-to-create-lists-using-list-comprehension)
    - [How to iterate over Pandas DataFrame](#243-how-to-iterate-over-pandas-dataframe)

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

# Day 25: Working with CSV Data and the Pandas Library

## 228: Reading CSV Data in Python

### Opening files in Python
We can open files in Python and populate contents in a list in the following way:

```python
with open("filepath.extension") as file:
    data = file.readlines()
```

When working with .csv files we can alternatively use `csv` library for reading data:

```python
import csv
with open("filepath.extension") as data_file:
    data = csv.reader(data_file)
```

We can also use `pandas` library to read csv files. The `pandas` documentation is available [here](https://pandas.pydata.org/docs/index.html)

```python
import pandas
data = pandas.read_csv("filepath.extension")
print(data)
```

## 229: DataFrames & Series: Working With Rows & Columns

| Type                                                                   | Definition                                           |
|------------------------------------------------------------------------|------------------------------------------------------|
| [***DataFrame***](https://pandas.pydata.org/docs/reference/frame.html) | Represents the whole table                           |
| [***Series***](https://pandas.pydata.org/docs/reference/series.html)   | Represents the row or column (almost as a List type) |

# Day 26: List Comprehension

## 235: How to create lists using List Comprehension
* List Comprehension is a unique task for Python Programming Language, and many of the other programming languages don't
even have this feature.
* List Comprehension is mainly used to save up space when writing code.

The universal idea behind list comprehension can be expressed using the following code:
```python
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
# Where:
# n + 1 is condition and how the input variable will be modified
# n is the variable that will be modified
# numbers is the list, which contains all variables "n" that will be modified using the condition "n + 1"
```

* List comprehension can work not only with lists, but also with tuples, strings, ranges or any other sequential data
type
* We can also use conditional formatting in List Comprehension. We can achieve this in the following way:
```python
numbers = [1, 2, 3]
new_list = [n for n in numbers if n < 3]
# Where:
# n is the input variable
# numbers is the list, which contains all variables "n" that will be added to the new_list if the condition is met
# n < 3 is the filtering condition 
```

## 243: How to iterate over Pandas DataFrame
* We can loop through DataFrame by using the same approaches that we use on dictionaries.
* Pandas also has an inbuilt method `iterrows()` which iterates the dictionary by rows not columns. For examples see:
  [Lecture 243 Code](/Lessons/Day26/L243main.py)

# Day 28: Tkinter, Dynamic Typing and the Pomodoro Clock 
