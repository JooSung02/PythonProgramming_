from tkinter import *

window = None

canvas = None

XSIZE, YSIZE = 256, 256

window = Tk()
canvas = Canvas(window, height= XSIZE, width= YSIZE)

canvas.pack()

paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")
window.mainloop()