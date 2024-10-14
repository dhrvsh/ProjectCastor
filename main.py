import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Project Castor')
screen = pygame.display.set_mode((1920, 1080), 0, 32)
clock = pygame.time.Clock()

pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]


backdrop = pygame.transform.scale(pygame.image.load("space.jpg"), (1920, 1080))

planetA = pygame.transform.scale(pygame.image.load("planetA.png"), (300, 300))
planetB = pygame.transform.scale(pygame.image.load("planetB.png"), (400, 400))
planetC = pygame.transform.scale(pygame.image.load("planetC.png"), (250, 250))
planetD = pygame.transform.scale(pygame.image.load("planetD.png"), (300, 300))
planetE = pygame.transform.scale(pygame.image.load("planetE.png"), (300, 300))

buttonPressed = ""

ship = pygame.transform.scale(pygame.image.load("ship.png"), (64, 64))
shipx = 30
shipy = 30
motion = [0, 0]

font = pygame.font.Font(None, 36)

# Create a flag to indicate if a collision has occurred
collision_flag = False

resetScreen = True

while True:
    if resetScreen == True:
        screen.fill((0, 0, 0))
        screen.blit(backdrop, (0, 0))

        screen.blit(planetA, (100, 50))
        screen.blit(planetB, (800, 300))
        screen.blit(planetC, (200, 600))
        screen.blit(planetD, (1500, 50))
        screen.blit(planetE, (1400, 650))

        screen.blit(ship, (shipx, shipy))
        if abs(motion[0]) < 0.1:
            motion[0] = 0
        if abs(motion[1]) < 0.1:
            motion[1] = 0
        shipx += motion[0] * 10
        shipy += motion[1] * 10

    # Check for collision with each planet
    if shipx + 64 >= 100 and shipx <= 400 and shipy + 64 >= 50 and shipy <= 350:
        collision_flag = True
        planetTouched = "A"
        
    elif shipx + 64 >= 800 and shipx <= 1200 and shipy + 64 >= 300 and shipy <= 700:
        collision_flag = True
        planetTouched = "B"
        
    elif shipx + 64 >= 200 and shipx <= 450 and shipy + 64 >= 600 and shipy <= 850:
        collision_flag = True
        planetTouched = "C"
        
    elif shipx + 64 >= 1500 and shipx <= 1800 and shipy + 64 >= 50 and shipy <= 350:
        collision_flag = True
        planetTouched = "D"
        
    elif shipx + 64 >= 1400 and shipx <= 1700 and shipy + 64 >= 650 and shipy <= 950:
        collision_flag = True
        planetTouched = "E"
    else:
        collision_flag = False
        resetScreen = True
        planetTouched = ""
        

    for event in pygame.event.get():

        if collision_flag:
            if event.type == pygame.JOYBUTTONDOWN:
                buttonID = event.button
                if buttonID == 0:
                    screen.fill((0, 0, 0))
                    resetScreen = False

        if collision_flag:
            if event.type == pygame.JOYBUTTONDOWN:
                buttonID = event.button
                if buttonID == 5:
                    screen.fill((0, 0, 0))
                    resetScreen = True


        if event.type == JOYAXISMOTION:
            axis = event.axis
            value = event.value

            if event.axis < 2:
                motion[event.axis] = event.value

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)