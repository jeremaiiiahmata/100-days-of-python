print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm : "))
age = int(input("What is your age : "))
bill = 0

# If-Else statement
if height > 120 :
    print("You can ride the rollercoaster.")
    if age <= 12 :
        bill = 5
    elif age <= 18 :
        bill = 7
    elif 45 <= age <= 55:
        bill = 0
    else :
        bill = 12

    print(f"You will pay ${bill}")

    doesIncludePhoto = input("Do you want to have a photo taken? Type 'y' for yes and 'n' for no :")

    if doesIncludePhoto == 'y' :
        bill += 3
        print(f"Additional fee of $3")

    print(f"Your final bill is ${bill}")

else :
    print("Sorry, you can't ride the rollercoaster.")


