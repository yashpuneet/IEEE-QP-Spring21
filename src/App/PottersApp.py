from serial import Serial
from tkinter import *
import pygame
import time

pygame.init()
pygame.mixer.init()

bgm = "BackgroundMusic.mp3"
bgmusic = pygame.mixer.music.load(bgm)
pygame.mixer.music.play(-1)

baud_rate = 9600
port = 'COM5' #May need to be changed when using Bluetooth

#conn = Serial(port, baud_rate, timeout=1)

#conn.write("t")
#moistureThreshold = conn.readline()

#conn.write("i")
#lightThreshold = conn.readline()

potters = Tk()
potters.title("The Potters")
potters.attributes('-fullscreen', True)

healthVal = 100
health = "Health: " + str(healthVal) + "%"

levelVal = 0 #Might implement database/SD card read
level = "Level: " + str(levelVal)

happinessVal = 2
happiness = "Happiness: " + str(happinessVal)

recommendation = "Ask Above! Give me what I need :("

#conn.write("u")
username = "The Potters - Will Read from Pot" #replace with conn.readline()

friendName = ""

def Close():
    potters.destroy()

def Moisture():
    print("moisture") #Delete
    #conn.write("m")
    #moisture = conn.readline()

def Light():
    print("light") #Delete
    #conn.write("l")
    #light = conn.readline()

def Feed():
    print("feed") #Delete
    #conn.write("f")

def Recommend():
    print("recommend") #Delete
    #conn.write("m")
    #moisture = conn.readline()
    #time.sleep(1)
    #conn.write("l")
    #light = conn.readline()
    #time.sleep(1)
    #if(moisture < moistureThreshold)

def MakeFriend():
    print("Make Friend")
    #conn.write("s")

bg = PhotoImage(file = "GreatHall.png") 
bglabel = Label(potters, image=bg)
bglabel.place(x=0, y=0, relwidth=1, relheight=1)

usernameLabel = Label(potters, text = username, font = ("Arial", 14))
usernameLabel.place(relx = 0.1, rely = 0.05, width = 400)

plant = PhotoImage(file = "Mandrake.png") #Will change to read from Pot
plantlabel = Label(potters, image=plant)
plantlabel.place(relx = 0.1, rely = 0.1, width=400, height=494)

exit = Button(potters, text="Exit", command=Close)
exit.place(relx=0.45, rely=0.9, relwidth=0.1, relheight=0.05)

levelLabel = Label(potters, text = level, font=("Arial", 18))
levelLabel.place(relx=0.4, rely = 0.1, relwidth = 0.4)

healthLabel = Label(potters, text = health, font=("Arial", 18))
healthLabel.place(relx=0.4, rely = 0.2, relwidth = 0.4)

happinessLabel = Label(potters, text = happiness, font=("Arial", 18))
happinessLabel.place(relx=0.4, rely = 0.3, relwidth = 0.4)

feed = Button(potters, text="Feed", font = ("Arial", 14), command=Feed)
feed.place(relx = 0.45, rely = 0.4, relwidth = 0.1)

recommend = Button(potters, text="Ask", font=("Arial", 14), command=Recommend)
recommend.place(relx = 0.65, rely = 0.4, relwidth=0.1)

recommendationLabel = Label(potters, text=recommendation, font=("Arial", 14))
recommendationLabel.place(relx = 0.4, rely = 0.5, relwidth = 0.4)

makeFriend = Button(potters, text="Make a Friend!", font=("Arial", 14), command=MakeFriend)
makeFriend.place(relx = 0.5, rely = 0.6, relwidth = 0.2)

bglabel.pack()

#conn.close()

potters.mainloop()
