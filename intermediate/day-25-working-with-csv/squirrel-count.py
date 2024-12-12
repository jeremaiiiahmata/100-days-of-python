import pandas

squirrelData = pandas.read_csv("./squirrel-count.csv")


grayCount = len(squirrelData[squirrelData["Primary Fur Color"] == "Gray"])
cinnamonCount = len(squirrelData[squirrelData["Primary Fur Color"] == "Cinnamon"])
blackCount = len(squirrelData[squirrelData["Primary Fur Color"] == "Black"])

print(grayCount)
print(cinnamonCount)
print(blackCount)

squirrelDict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grayCount, cinnamonCount, blackCount]
}

df = pandas.DataFrame(squirrelDict)
df.to_csv("squirrel-color-count.csv")