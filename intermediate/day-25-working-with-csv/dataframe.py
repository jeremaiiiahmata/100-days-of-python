import pandas

dataDictionary = {
    "students" : ["Jerem", "Josh", "Athena"],
    "scores" : [99,96,100]
}

dataF = pandas.DataFrame(dataDictionary)
print(dataF)

dataF.to_csv("new_data.csv")