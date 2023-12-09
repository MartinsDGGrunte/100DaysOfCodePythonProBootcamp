import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].tolist()


def calculate_avg(int_list):
    sum_value = sum(int_list)
    num_days = len(int_list)
    return round(sum_value / num_days, 2)


# Conventional Python Way
print(calculate_avg(temp_list))

# Pandas way
print(round(data["temp"].mean(), 2))

# Print maximum value
print(data["temp"].max())

# print row which has value
print(data[data.day == "Monday"])

# get row where temperature is maximum
print(data[data.temp == data.temp.max()])

# convert mondays temperature to Fahrenheit
monday_data = data[data.day == "Monday"]
monday_temp = monday_data.temp[0]


def convert_to_fahrenheit(temperature_in_c):
    return temperature_in_c * (9 / 5) + 32


print(convert_to_fahrenheit(monday_temp))

# Creating our own DataFrame
data = {
    "name": ["Joey", "Ross", "Chandler"],
    "grade": [57, 72, 67]
}

grades = pandas.DataFrame(data)
print(grades)

# We can create a csv file from pandas data frame
grades.to_csv("grades.csv")
