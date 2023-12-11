numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
# Where:
# n + 1 is condition and how the input variable will be modified
# n is the variable that will be modified
# numbers is the list, which contains all variables "n" that will be modified using the condition "n + 1"
print(f'Base list is: {numbers}')
print(f'Created list is: {new_list}')


# List comprehension can work not only with lists, but also with tuples, strings, ranges or any other sequential data
# type

doubled_numbers = [number * 2 for number in range(1, 5)]
print(f'Original numbers are: {[1, 2, 3, 4]}')
print(f'Doubled numbers are: {doubled_numbers}')

names = ["Anna", "Martins", "John", "Isabella", "Carla", "Johnathan"]
short_names = [name.upper() for name in names if len(name) < 5]
print(f'All names: {names}')
print(f'Short names: {short_names}')
