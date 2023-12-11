# 1. Read file
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# 2. Create dictionary
dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

# 3. Take user input and convert to list of letters
name = input("Enter a name that you want to convert to nato phonetic alphabet: ").upper()
letter_list = list(name)

# 4. Create a list of nato phonetics
end_list = [dictionary[value] for value in letter_list]
print(end_list)
