# Unlimited Positional Arguments
def add (*args):
    total = 0

    for i in args:
        total += i

    return total

print(f"The sum of 1 - 4 is : {add(1,2,3,4)}")


print("\n\n-----= Unlimited Keyword Arguments =-----")
# Unlimited Keyword Arguments

class Car :
    def __init__(self, **kw):
        if kw.get("model") :
            self.model = kw.get("model") # Use the .get() method so even if the argument is called but has no value, it will just return false
        else :
            self.model = "Honda Civic"
        self.speed = kw.get("speed")
        self.color = kw.get("color")

    def printValues(self):
        if self.model:
            print(f"Model : {self.model}")
        else :
            print("No value given in model.")

        print(f"Color : {self.color}")
        print(f"Speed : {self.speed}")

car = Car(model="Toyota Fortuner", color="Midnight Black", speed="400")

car.printValues()

# print(f"Model : {car.model}")
# print(f"Color : {car.color}")
# print(f"Speed : {car.speed}")

