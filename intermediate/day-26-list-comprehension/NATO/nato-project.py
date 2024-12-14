import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv") #Reads the file in .csv format, one of the features of pandas
print(data)
#Using a dict comprehension, for each index and row in the data, create a new key and value
#New key = row.letter & New value = row.code
#data.iterrows() -> loops through each row of the .csv
#(index, rows) unpacks the  key-value pairs
#index -> built-in variable and can't be changed
#rows -> a pandas series object that represents the data of the current row.
natoDictionary = {row.letter:row.code for (index, row) in data.iterrows()}
print(natoDictionary)

message = input("Enter a message : ")

#Using a list comprehension,
natoMessage = [natoDictionary[letter.upper()] for letter in message]

print(natoMessage)