from tkinter import *

window = Tk()

photo = PhotoImage(file= r"C:\Users\jooro\OneDrive\바탕 화면\PythonProgramming_\WindowProgramming\\dog.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()
