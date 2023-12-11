# Dictionary Comprehension
import random

# create a list of names
names = ["Anna", "Martins", "John", "Isabella", "Carla", "Johnathan"]

# create a dictionary using dictionary comprehension
scores_dictionary = {n: random.randint(1, 100) for n in names}
print(scores_dictionary)
# Where:
# scores_dictionary is name of the dictionary
# n is key in our new dictionary "scores_dictionary" AND value in the list "names"
# random.choice(range(1, 101)) is a randomly generated value in our new dictionary "scores_dictionary"
# "names" is the list which contains all student names "n".

passed_students = {key: value for (key, value) in scores_dictionary.items() if value >= 60}
print(passed_students)
