from tkinter import *
import random

btnList = [None] * 9
fnameList = ["bee.gif", "cake.gif", "camera.gif", "clover.gif", "earth.gif", "flower.gif", "strawberry.gif", "sun.gif", "watermelon.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.geometry("400x400")

for i in range(0, 9) :
    photoList[i] = PhotoImage(file=r"C:\Users\jooro\OneDrive\바탕 화면\PythonProgramming_\Week9\\" +fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

random.shuffle(btnList)

for i in range(0, 3) :
    for k in range(0, 3) :
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 130
    xPos = 0
    yPos += 130

window.mainloop()