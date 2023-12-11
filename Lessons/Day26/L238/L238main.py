with open("file1.txt") as file1:
    values_f1 = file1.readlines()

with open("file2.txt") as file2:
    values_f2 = file2.readlines()

result = [int(value.replace("\n", "")) for value in values_f1 if (value in values_f2)]
print(result)
