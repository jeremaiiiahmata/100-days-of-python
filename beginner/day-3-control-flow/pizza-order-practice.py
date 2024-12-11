print("Welcome to the Best Pizza Place!")

pizzaSize = input("What size of pizza do you want? S, M, or L : ")
withPepperoni = input("Do you want pepperoni on your pizza? Y or N : ")
withExtraCheese = input("Do you want extra cheese? Y or N : ")
bill = 0

if pizzaSize == 'S' :
    bill += 15
elif pizzaSize == 'M' :
    bill += 20
elif pizzaSize == 'L' :
    bill += 25
else :
    print("Wrong input. Please try again.")

if withPepperoni == 'Y' :
    if pizzaSize == 'S' :
        bill += 2
    else :
        bill += 3

if withExtraCheese == 'Y' :
    bill += 1

print("\n---------PIZZA RECEIPT---------")
print(f"Pizza Size : ${pizzaSize}")
print(f"With Pepperoni? : ${withPepperoni}")
print(f"With Extra Cheese? : ${withExtraCheese} ")
print(f"Your total bill is ${bill}")
print("---------PIZZA RECEIPT---------")

amount = int(input("\nEnter amount : "))

print(f"You have entered an amount of ${amount}")
if amount >= bill :
    change = amount - bill
    print(f"\n\nYour Total Bill : ${bill}")
    print(f"Cash : ${amount}")
    print(f"Change : ${change}")

else :
    print("The amount you have entered is less than the bill. Please try again.")




