from coffee_data import coffee

vendoProperties = {
    "Water" : 10000,
    "Milk" : 10000,
    "Coffee" : 10000,
    "BaseAmount" : 0
}

def processCoffee(coffeeType, vendoProperties) :

    vendoProperties["Water"] -= coffee[coffeeType]["Water"]
    vendoProperties["Milk"] -= coffee[coffeeType]["Milk"]
    vendoProperties["Coffee"] -= coffee[coffeeType]["Coffee"]
    vendoProperties["BaseAmount"] += coffee[coffeeType]["Price"]

    return vendoProperties

def processUserChange(coffeeType, amountInserted) :

    price = coffee[coffeeType]["Price"]

    if amountInserted >= price :

        return float(amountInserted - price)

    else :

        return False

def checkResources(coffeeType, vendoProperties) :

    if vendoProperties["Water"] > coffee[coffeeType]["Water"] :

        if vendoProperties["Milk"] > coffee[coffeeType]["Milk"] :

            if  vendoProperties["Coffee"] > coffee[coffeeType]["Coffee"] :

                return True
    else :

        return False

def processDisplayForUser(coffeeType) :

    price = coffee[coffeeType]["Price"]

    print(f"Great Choice! That would be ${price}.")

def generateReport(vendoProperties) :
    print("\n")
    print("------------=====REPORT=====------------")
    print(f"Water : {vendoProperties["Water"]}")
    print(f"Milk : {vendoProperties["Milk"]}")
    print(f"Coffee : {vendoProperties["Coffee"]}")
    print(f"Profit : ${vendoProperties["BaseAmount"]}")
    print("------------=================------------")
    print("\n")

def generateReceipt(coffeeType, amountInserted) :

    print("\n")
    print("------------=====REPORT=====------------")
    print(f"Water : {coffee[coffeeType]["Water"]}")
    print(f"Milk : {coffee[coffeeType]["Milk"]}")
    print(f"Coffee : {coffee[coffeeType]["Coffee"]}")
    print(f"Amount Inserted : ${amountInserted}")
    print(f"Change : ${float(amountInserted - coffee[coffeeType]["Price"])}")
    print("------------=================------------")
    print("\n")


hasNotExit = True
isResourcesEnough = True

while hasNotExit and isResourcesEnough:

    coffeeType = input("What would you like? [Espresso, Latte, Cappuccino] : ").title()

    if coffeeType == "Exit":
        hasNotExit = False
    elif coffeeType == "Report":
        generateReport(vendoProperties)
    else :
        if checkResources(coffeeType, vendoProperties) :
            processDisplayForUser(coffeeType)

            print("\n")
            amountFromUser = float(input("Enter amount : "))

            print("\n")
            print("Brewing...")
            price = processCoffee(coffeeType, vendoProperties)

            if not price :
                print("\n")
                print("Invalid Amount, Money refunded.")
                hasNotExit = False

            generateReceipt(coffeeType, amountFromUser)

        else :
            print("\n")
            print("Vendo does not have enough resources.")
            isResourcesEnough = False