# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import pandas

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)


# print(data["temp"].mean())
# print(data["temp"].max())
# average = sum(temp_list)/len(temp_list)
# print(average)


# print(data["condition"])
#Alternative to using scquare bracket notation
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = (monday_temp * 9/5) + 32
# # print(monday.condition)
# print(monday_temp_F)
# print(monday.condition)


#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")

############Angela's way###################
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#
# # temperatures.pop(0)
# print(temperatures)

###############################Squirrel data##########################################
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # print(data["Primary Fur Color"])
# gray_s = len(data["Primary Fur Color"] == "Gray")
# red_s = len(data["Primary Fur Color"] == "Red")
# black_s = len(data["Primary Fur Color"] == "Black")
#
# ########## Your Way ############
# cinnamon_s = (data["Primary Fur Color"] == "Cinnamon").count()
#
# data_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [gray_s, red_s, black_s ]
# }
# print(data_dict)

# s_data = pandas.DataFrame(data_dict)
# s_data.to_csv("new_squirrel_data.csv")


# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


############My way###################
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         temperatures.append((row[1]))
#     res = [eval(i) for i in temperatures[1:]]

# print(res)