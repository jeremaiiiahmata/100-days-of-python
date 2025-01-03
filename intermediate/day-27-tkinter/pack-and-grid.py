from tkinter import *

window = Tk()
window.title("Packs vs Grids")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = Label()
label.config(text="Label", font=("Arial", 24, "bold"))

button = Button()
button.config(text="Button")

button2 = Button()
button2.config(text="New Button")

entry = Entry()
entry.config(width=10)

label.grid(column=0, row=0)
button2.grid(column=2, row=0)
button.grid(column=1, row=1)
entry.grid(column=3, row=2)

window.mainloop()