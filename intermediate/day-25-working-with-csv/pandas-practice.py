import pandas

data = pandas.read_csv("data/weather_data.csv")

print(data)
print(data["temp"])

# Converts the data from the csv to a dictionary using pandas :
dataDictionary = data.to_dict()
print(f"Dictionary: {dataDictionary}")

# Converts the data from the csv to a list using pandas :
dataList = data["temp"].to_list()
print(f"Data List : {dataList}")

# ---- Getting the maximum value of the series
print(data["temp"].max())

#---- Getting the average :

# total = 0
# for data in dataList:
#     total += data
#
# # average = total/len(dataList)
# # print(f"Average : {average}")

# We can use this :

print(data["temp"].mean())

# ---- TWO WAYS OF ACCESSING THE DATA
print(data["temp"]) #Square brackets
print(data.temp) #Dot notation

# ---- Accessing a specific row through conditions
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"]
print(monday)
mondayTemperature = monday.temp[0] #Access the first index, since monday.temp returns an object
tempFahrenheit = mondayTemperature * 9/5 + 32
print(tempFahrenheit)