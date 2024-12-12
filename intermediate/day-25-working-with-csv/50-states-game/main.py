from turtle import Screen

screen = Screen()
image = "blank_states_img.gif"
screen.bgpic(image)

def getMouseClick(x, y):
    answer = screen.textinput(title="Enter State : " )
    print(x, y)

screen.onscreenclick(getMouseClick)

screen.mainloop()