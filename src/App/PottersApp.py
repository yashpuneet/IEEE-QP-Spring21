#from serial import Serial
import pygame
import random
import sys
import time

pygame.init()
pygame.mixer.init()

bgm = "bgm.mp3"
bgmusic = pygame.mixer.music.load(bgm)
pygame.mixer.music.play(-1)

healthVal = 100
health = "Health: " + str(healthVal) + "%"

levelVal = 0 #Might implement database/SD card read
level = "Level: " + str(levelVal)

happinessVal = 10
happiness = "Happiness: " + str(happinessVal)

foodCount = 0
food = "Feeds: " + str(foodCount)

helpCount = 0
helpStr = "Recommendations: " + str(helpCount)

#recommendation = "Ask Above! Give me what I need :("

#conn.write("u")
#username = "The Potters - Will Read from Pot" #replace with conn.readline()

potters = pygame.display.set_mode((1000, 600))

clockRate = 60
clock = pygame.time.Clock()

bg = pygame.image.load("GreatHall.png")
sprite = pygame.image.load("plant.png")
weed = pygame.image.load("weed.png")
water = pygame.image.load("water.png")
rec = pygame.image.load("rec.png")

x, y = potters.get_size()
bg = pygame.transform.scale(bg, [x, y])
weed1 = pygame.transform.scale(weed, [60, 100])
weed2 = pygame.transform.scale(weed, [60, 100])
weed3 = pygame.transform.scale(weed, [60, 100])
water = pygame.transform.scale(water, [50, 100])
rec = pygame.transform.scale(rec, [50, 100])

pygame.display.set_caption('The Potters')

potters.blit(bg, [0, 0])

def drawPlant(w, h):
    potters.blit(bg, [0, 0])
    potters.blit(sprite, [w, h])

def writeText(text, size, x, y):
    font = pygame.font.SysFont('arial', size)
    words = font.render(text, True, (0,0,0))
    potters.blit(words, [x, y])

def createWeed1(b):
    potters.blit(weed1, [b,400])

def createWeed2(e):
    potters.blit(weed2, [e,400])

def createWeed3(f):
    potters.blit(weed3, [f,400])

def createWater(c):
    potters.blit(water, [c,150])

def createRec(d):
    potters.blit(rec, [d,150])
    
running = True

w = 100
w_change = 0

h = 360

weedCount = 1
waterCount = 1
recCount = 1

weed1Pos = random.randint(100, 900)
weed2Pos = random.randint(100, 900)
weed3Pos = random.randint(100, 900)
waterPos = random.randint(100, 900)
recPos = random.randint(100, 900)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                w_change = -5
            elif event.key == pygame.K_RIGHT:
                w_change = 5
            elif event.key == pygame.K_a:
                shoot = pygame.mixer.music.load("shoot.mp3")
                pygame.mixer.music.play(0)
                if weedCount == 1:
                    if weed1Pos < w:
                        weedCount = 0
                    if weed2Pos < w:
                        weedCount = 0
                    if weed3Pos < w:
                        weedCount = 0
            elif event.key == pygame.K_d:
                shoot = pygame.mixer.music.load("shoot.mp3")
                pygame.mixer.music.play(0)
                if weedCount == 1:
                    if weed1Pos > w:
                        weedCount = 0
                    if weed2Pos > w:
                        weedCount = 0
                    if weed3Pos > w:
                        weedCount = 0
            elif event.key == pygame.K_w:
                shoot = pygame.mixer.music.load("shoot.mp3")
                pygame.mixer.music.play(0)
                if w in range(waterPos-80, waterPos+80):
                    foodCount = foodCount + 0.25
                    food = "Feeds: " + str(foodCount)
                    weedCount = 0
                    waterCount = 0
                if w in range(recPos-80, recPos+80):
                    helpCount = helpCount + 0.25
                    helpStr = "Recommendations: " + str(helpCount)
                    recCount = 0
                    weedCount = 0
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                w_change = 0

    if w > x - 150:
        w = 0

    if w < 0:
        w = x - 150

    w = w + w_change        
    drawPlant(w, h)
    if weedCount < 1:
        weed1Pos = random.randint(100, 900)
        weed2Pos = random.randint(100, 900)
        weed3Pos = random.randint(100, 900)
        weedCount = 1

    if waterCount < 1:
        waterPos = random.randint(100, 900)
        waterCount = 1

    if recCount < 1:
        recPos = random.randint(100, 900)
        recCount = 1
        
    if w in range(weed1Pos - 30, weed1Pos + 30):
        healthVal = healthVal - 10
        health = "Health: " + str(healthVal) + "%"
        weedCount = 0
        print("crash")

    if w in range(weed2Pos - 30, weed2Pos + 30):
        healthVal = healthVal - 10
        health = "Health: " + str(healthVal) + "%"
        weedCount = 0
        print("crash")

    if w in range(weed3Pos - 30, weed3Pos + 30):
        healthVal = healthVal - 10
        health = "Health: " + str(healthVal) + "%"
        weedCount = 0
        print("crash")

    if healthVal < 1:
        waterPos = 1500
        recPos = 1500
        weed1Pos = 1500
        weed2Pos = 1500
        weed3Pos = 1500
        happinessVal = happinessVal - 1
        healthVal = 100
        happiness = "Happiness: " + str(happinessVal)
        health = "Health: " + str(healthVal) + "%"

    createWater(waterPos)
    createRec(recPos)
    createWeed1(weed1Pos)
    createWeed2(weed2Pos)
    createWeed3(weed3Pos)
    writeText(health, 20, 800, 15)
    writeText(level, 20, 800, 45)
    writeText(happiness, 20, 800, 75)
    writeText(food, 20, 15, 45)
    writeText(helpStr, 20, 15, 15)

    pygame.display.update()
    clock.tick(60)
