#Dictionary
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

#Nested List in a Dictionary
travel_logs = {
    "France" : ["Paris", "Lille", "Dijon"]
}

print(travel_logs["France"][1])

#Nested List
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

#Nested Dictionary

countries = {
    "France" : {
        "timesVisited" : 12,
        "citiesVisited" : ["Paris", "Lille", "Dijon"]
    },
    "Germany" : {
        "timesVisited" : 9,
        "citiesVisited" : ["Berlin", "Hamburg", "Stuttgart"]
    }
}

#Accessing
print(countries["Germany"]["citiesVisited"][2])