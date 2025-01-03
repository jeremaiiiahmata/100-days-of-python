from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

def convertToKilometers() :
    miles = float(userInput.get())
    miles *= 1.609

    labelValue.config(text=str(miles))

# -- is equal to label
labelText = Label()
labelText.config(text="is equal to")
labelText.grid(column=0, row=1)

# -- holder for value
labelValue = Label()
labelValue.config(text="0")
labelValue.grid(column=1, row=1)

# -- km
labelKm = Label()
labelKm.config(text="km")
labelKm.grid(column=2, row=1)

# -- miles
labelMiles = Label()
labelMiles.config(text="miles")
labelMiles.grid(column=2, row=0)

# -- user's input
userInput = Entry()
userInput.config(width=10)
userInput.grid(column=1, row=0)

# -- button
button = Button()
button.config(text="Convert", command=convertToKilometers)
button.grid(column=1, row=2)


window.mainloop()