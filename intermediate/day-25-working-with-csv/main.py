import csv

with open("./weather_data.csv") as file :
    data = csv.reader(file)
    temperature = []

    for temp in data :
        if temp[1] != "temp":
            temperature.append(int(temp[1]))

    print(temperature)