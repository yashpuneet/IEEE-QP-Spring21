import serial
from tkinter import *

potters = Tk()
potters.title("The Potters")
potters.attributes('-fullscreen', True)

bg = PhotoImage(file = "GreatHall.png")
bglabel = Label(potters, image=bg)
bglabel.place(x=0, y=0, relwidth=1, relheight=1)

potters.mainloop()
