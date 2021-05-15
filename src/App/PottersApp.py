from serial import Serial
from tkinter import *

baud_rate = 9600
port = 'COM5' #May need to be changed when using Bluetooth

#conn = Serial(port, baud_rate, timeout=1)

potters = Tk()
potters.title("The Potters")
potters.attributes('-fullscreen', True)

healthVal = 100
health = "Health: " + str(healthVal) + "%"

levelVal = 0 #Might implement database/SD card read
level = "Level: " + str(levelVal)

happinessVal = 2
happiness = "Happiness: " + str(happinessVal)

def Close():
    potters.destroy()

def Moisture():
    healthVal = 100
    #conn.write("m")
    #moisture = conn.readline()

def Light():
    levelVal = 100
    #conn.write("l")
    #light = conn.readline()

def Feed():
    happinessVal = 100
    #conn.write("f")

bg = PhotoImage(file = "GreatHall.png")
bglabel = Label(potters, image=bg)
bglabel.place(x=0, y=0, relwidth=1, relheight=1)

plant = PhotoImage(file = "Mandrake.png")
plantlabel = Label(potters, image=plant)
plantlabel.place(relx = 0.1, rely = 0.1, relwidth = 0.3, relheight = 0.7)

exit = Button(potters, text="Exit", command=Close)
exit.place(relx=0.45, rely=0.9, relwidth=0.1, relheight=0.05)

bglabel.pack()

#conn.close()

potters.mainloop()
