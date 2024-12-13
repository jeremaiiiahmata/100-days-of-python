import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

natoDictionary = {row.letter:row.code for (index, row) in data.iterrows()}
print(natoDictionary)

message = input("Enter a message : ")

natoMessage = [natoDictionary[letter.upper()] for letter in message]

print(natoMessage)