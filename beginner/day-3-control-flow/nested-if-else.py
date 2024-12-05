print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm : "))
age = int(input("What is your age : "))

# If-Else statement
if height > 120 :
    print("You can ride the rollercoaster.")
    if age <= 12 :
        print("You will pay $5")
    elif age <= 18 :
        print("You will pay $7")
    else :
        print("You will pay $12")
else :
    print("Sorry, you can't ride the rollercoaster.")


