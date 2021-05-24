#from serial import Serial
import pygame
#import sys
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

happinessVal = 2
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

x, y = potters.get_size()
bg = pygame.transform.scale(bg, [x, y])

pygame.display.set_caption('The Potters')

potters.blit(bg, [0, 0])

def drawPlant(w, h):
    potters.blit(bg, [0, 0])
    potters.blit(sprite, [w, h])

def writeText(text, size, x, y):
    font = pygame.font.SysFont('arial', size)
    words = font.render(text, True, (0,0,0))
    potters.blit(words, [x, y])
    

running = True

w = 100
w_change = 0

h = 360

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                w_change = 0

    if w > x - 150:
        w = 0

    if w < 0:
        w = x - 150
    
    w = w + w_change
    drawPlant(w, h)
    writeText(health, 20, 800, 15)
    writeText(level, 20, 800, 45)
    writeText(happiness, 20, 800, 75)
    writeText(food, 20, 15, 45)
    writeText(helpStr, 20, 15, 15)
    
    pygame.display.update()
    clock.tick(60)




