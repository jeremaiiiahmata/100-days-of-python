from tkinter import *

window = Tk()

#Label Component
label = Label(text="Label 1", font=("Arial", 24, "bold"))
label.pack() #Place it into the screen, automatically centers it in the GUI.

#Button Component
def buttonClick():
    userInput = input.get()
    label.config(text= userInput)

btn = Button()
btn.config(text="Click Me", command=buttonClick)
btn.pack()

#Entry Component - For inputs
input = Entry(width=10)
input.pack()




window.minsize(width=500, height=300)
window.title("First GUI")
window.mainloop() #Prevents the windows from exiting and listens on events
