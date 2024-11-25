#Tip Calculator
print("Welcome to the tip calculator!")

#Gets the input needed
totalBill = input("What was the total bill : $")
tip = input("How much tip would you like to give? 10, 12, or 15? :")
numberOfPeople = input("How many people to split the bill : ")

#Calculation of tip
billTip = ((int(tip) / 100) * float(totalBill))
splittedBill = round((float(totalBill) + billTip) / int(numberOfPeople), 2)

#Printing of output
print(f"Each person should pay : ${splittedBill}")