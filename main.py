import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(gray_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
