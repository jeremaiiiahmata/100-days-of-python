from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

hasNotExit = True
isResourcesEnough = True

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()


while hasNotExit and isResourcesEnough:

    coffeeType = input(f"What would you like? {menu.get_items()} : ").title()

    if coffeeType.lower() == "off" :
        hasNotExit = False
    elif coffeeType.lower() == "report" :
        moneyMachine.report()
        coffeeMaker.report()
    else :
        drink = menu.find_drink(coffeeType.lower())

        print(f"Great Choice! That would be ${drink.cost}")

        if coffeeMaker.is_resource_sufficient(drink):
            print("\nResources are enough...")
            print("\nMaking coffee...")
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)







