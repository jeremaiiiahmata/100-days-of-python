import random

password = []
temp = ""
finalPassword = ""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letterAmount= int(input("How many letters would you like in your password? :"))
symbolAmount = int(input(f"How many symbols would you like? :"))
numberAmount = int(input(f"How many numbers would you like? :"))

#Easy

for i in range(1, letterAmount+1) :
    randomValue = random.choice(letters)
    password.append(randomValue)

for i in range(1, symbolAmount+1) :
    randomValue = random.choice(symbols)
    password.append(randomValue)

for i in range(1, numberAmount+1) :
    randomValue = random.choice(numbers)
    password.append(randomValue)

for i in password :
    finalPassword += i

print(f"Your password is : {finalPassword}")


#Hard
finalPassword = ""
random.shuffle(password)

for i in password :
    finalPassword += i

print(f"Your shuffled password is : {finalPassword}")

#Without user's input

randomGeneratedPassword = ""
randomGeneratedPasswordList = []

randomLettersAmount = random.randint(3,11)
randomSymbolsAmount = random.randint(3,11)
randomNumbersAmount = random.randint(3,11)

for i in range (1, randomLettersAmount) :
    randomGeneratedPasswordList.append(random.choice(letters))


for i in range(1, randomSymbolsAmount):
    randomGeneratedPasswordList.append(random.choice(symbols))

for i in range(1, randomNumbersAmount):
    randomGeneratedPasswordList.append(random.choice(numbers))

random.shuffle(randomGeneratedPasswordList)

for i in randomGeneratedPasswordList :
    randomGeneratedPassword += i

print(f"Your random generated password is : {randomGeneratedPassword}")


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P