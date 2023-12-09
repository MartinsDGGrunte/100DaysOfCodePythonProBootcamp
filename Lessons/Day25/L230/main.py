# import data
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(list(squirrel_data["Primary Fur Color"]))
squirrel_fur_color_data = list(squirrel_data["Primary Fur Color"])

gray = 0
cinnamon = 0
black = 0
for color in squirrel_fur_color_data:
    if color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Black":
        black += 1

data = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, cinnamon, black]
}

end_dataframe = pandas.DataFrame(data)
end_dataframe.to_csv("squirrel_count.csv")