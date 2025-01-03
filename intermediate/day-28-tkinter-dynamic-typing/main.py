from imghdr import tests
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#FFFFFF"
FONT_NAME = "Poppins"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
sets = 0
counter = None

# ---------------------------- TIMER RESET ------------------------------- #

def resetTimer():
    window.after_cancel(counter)
    canvas.itemconfig(timer, text="00:00")
    timerLabel.config(text="Pomodoro Timer")
    checkmarkLabel.config(text="")

    global reps, sets
    reps = 0
    sets = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def addSet():
    global sets

    sets += 1
    checkmarkLabel.config(text="⭕" * sets)

def startTimer():
    global reps
    reps += 1
    print(reps)

    workSeconds = WORK_MIN * 60
    shortBreakSeconds = SHORT_BREAK_MIN * 60
    longBreakSeconds = LONG_BREAK_MIN * 60

    if not reps % 2 == 0 : #Checks if the rep is 1,3,5,7
        timerLabel.config(text="Work Mode")
        countDown(workSeconds)
        print("Work")
    else :
        if reps == 8: # Checks if the rep is the 8th one.
            timerLabel.config(text="20-Min Break!")
            countDown(longBreakSeconds)
            addSet()
            print("Long break.")
        else :
            timerLabel.config(text="5-Min Break!")
            countDown(shortBreakSeconds)
            addSet()
            print("Short break.")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countDown(count):
    print(count)
    minutes = math.floor(count/60) # 300/60 = 6, floors the value if there are decimal
    seconds = count % 60 # Returns the remainder of the division

    if minutes == 0 and seconds < 10 :
        canvas.itemconfig(timer, text=f"00:0{seconds}")
    elif minutes == 0 :
        canvas.itemconfig(timer, text=f"00:{seconds}")  # Changes the countdown label
    elif seconds < 10:
        canvas.itemconfig(timer, text=f"{minutes}:0{seconds}") #Changes the countdown label
    else :
        canvas.itemconfig(timer, text=f"{minutes}:{seconds}")

    if count > 0:
        global counter
        counter =  window.after(1000, countDown, count-1) #Delays for 1 second then calls the countDown function again where the count is subtracted by 1.
    else :
        startTimer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=PINK)

# -- Canvas
canvas = Canvas(width=400, height=224, bg=PINK, highlightthickness=0)
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(200, 112, image=tomatoImage)
timer = canvas.create_text(200, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# -- Timer label
timerLabel = Label()
timerLabel.config(text="Pomodoro Timer", fg=WHITE, bg=PINK, font=(FONT_NAME, 32, "bold"))
timerLabel.grid(column=1, row=0)

# -- Checkmark Label
checkmarkLabel = Label()
checkmarkLabel.config(text="", bg=PINK)
checkmarkLabel.grid(column=1, row=3)

# -- Start Button
startButton = Button()
startButton.config(text="Start", bg=YELLOW, font=(FONT_NAME, 12, "bold"), border=0, command=startTimer)
startButton.grid(column=0, row=2)

# -- Reset Button
resetButton = Button()
resetButton.config(text="Reset", bg=YELLOW, font=(FONT_NAME, 12, "bold"), border=0, command=resetTimer)
resetButton.grid(column=2, row=2)



window.mainloop()