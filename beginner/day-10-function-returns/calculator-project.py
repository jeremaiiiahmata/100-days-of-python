#Simple Calculator project using dictionary and functions

newCalculation = True

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}

def calculator() :
    while newCalculation:

        continueCalculating = True

        firstNumber = float(input("What's the first number : "))
        for each in operations:
            print(each)
        operation = input("Pick an operation : ")
        secondNumber = float(input("What's the next number : "))

        result = operations[operation](firstNumber, secondNumber)

        while continueCalculating :
            print("\n")
            print(f"{firstNumber} {operation} {secondNumber} = {result}")


            print("\n")
            continueCalculate = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation :")

            if continueCalculate.lower() == 'y' :
                print("\n")
                for each in operations:
                    print(each)
                operation = input("Pick an operation : ")
                secondNumber = float(input("What's the next number : "))
                result = operations[operation](result, secondNumber)

            else :
                continueCalculating = False

calculator()

