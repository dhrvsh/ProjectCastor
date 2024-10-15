import sys
import pygame
from pygame.locals import *
import os


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-370, -800)


pygame.init()
pygame.display.set_caption('Project Castor')
screen = pygame.display.set_mode((1280, 800), 0, 32)
clock = pygame.time.Clock()

pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

# Load background and planets
backdrop = pygame.transform.scale(pygame.image.load("space.png"), (1280, 800))
planetA = pygame.transform.scale(pygame.image.load("planetA.png"), (200, 200))
planetB = pygame.transform.scale(pygame.image.load("planetB.png"), (250, 250))
planetC = pygame.transform.scale(pygame.image.load("planetC.png"), (300, 300))
planetD = pygame.transform.scale(pygame.image.load("planetD.png"), (200, 200))
planetE = pygame.transform.scale(pygame.image.load("planetE.png"), (200, 200))

# Create Rect objects for planets for collision detection
planetA_rect = pygame.Rect(150, 100, 200, 200)
planetB_rect = pygame.Rect(500, 250, 300, 300)
planetC_rect = pygame.Rect(150, 430, 250, 250)
planetD_rect = pygame.Rect(950, 100, 200, 200)
planetE_rect = pygame.Rect(1000, 500, 200, 200)

# Load ship
ship = pygame.transform.scale(pygame.image.load("U.png"), (64, 64))
ship_rect = pygame.Rect(ship.get_rect())  # Ship's Rect
shipx = 30
shipy = 30
motion = [0, 0]

biggerfont = pygame.font.Font("MajorMonoDisplay.ttf", 40)
font = pygame.font.Font("MajorMonoDisplay.ttf", 32)

planetTouched = None  # Initialize planetTouched as None

collision_flag = False
resetScreen = True

angle = 0
direction = "U"
mainapp = True



while True:
    if mainapp == False:
        screen.fill((0, 0, 0))
        screen.blit(backdrop, (0, 0))
        mainapp == True
    elif mainapp == True:
        if resetScreen == True:
            #Resetting screen and setting sprites
            screen.fill((0, 0, 0))
            screen.blit(backdrop, (0, 0))

            screen.blit(planetA, (150, 100))
            screen.blit(planetB, (500, 250))
            screen.blit(planetC, (150, 430))
            screen.blit(planetD, (950, 100))
            screen.blit(planetE, (1000, 500))

            screen.blit(ship, (shipx, shipy))
            
            planetTouched = None 
            
            # Moving depending on joystick movement
            if abs(motion[0]) < 0.1:
                motion[0] = 0
            if abs(motion[1]) < 0.1:
                motion[1] = 0
            shipx += motion[0] * 10
            shipy += motion[1] * 10
            
            if shipx <= -1 or shipx >= 1217:
                shipx -= motion[0] * 10
            if shipy <= 0 or shipy >= 737:
                shipy -= motion[1] * 10
            
            
            if (motion[0] * 10) > 0:
                direction = "R"
            elif (motion[0] * 10) < 0:
                direction = "L"
            elif (motion[1] * 10) > 0:
                direction = "D"
            elif (motion[1] * 10) < 0:
                direction = "U"
            else:
                pass
            
            ship = pygame.transform.scale(pygame.image.load(direction + ".png"), (64, 64))




            # "Converting" ship into a "rectangle"
            ship_rect.topleft = (shipx, shipy)
            
            # Check for collisions with planets
            if ship_rect.colliderect(planetA_rect):
                planetTouched = "A"
            if ship_rect.colliderect(planetB_rect):
                planetTouched = "B"
            if ship_rect.colliderect(planetC_rect):
                planetTouched = "C"
            if ship_rect.colliderect(planetD_rect):
                planetTouched = "D"
            if ship_rect.colliderect(planetE_rect):
                planetTouched = "E"

        for event in pygame.event.get():
            # Checking for joystick movement
            if event.type == JOYAXISMOTION:
                axis = event.axis
                value = event.value
                if event.axis < 2:
                    motion[event.axis] = event.value

            # Checking for buttons pressed
            if event.type == pygame.JOYBUTTONDOWN:
                buttonID = event.button
                # if buttonID == 5:
                    # DISPLAYSURF = pygame.display.set_mode((0, 0), (pygame.FULLSCREEN))
                if buttonID == 0:
                    # Making information window
                    if planetTouched != None:
                        resetScreen = False
                        screen.fill((0, 0, 0))
                        screen.blit(backdrop, (0, 0))
                        
                    


                        if planetTouched == "A":
                            planetname = "PSR B1257+12 c"
                            planetA = pygame.transform.scale(pygame.image.load(planetname + ".png"), (150, 150))
                            planetTouched = 0
                        elif planetTouched == "B":
                            planetname = "PSR B1257+12 d"
                            planetB = pygame.transform.scale(pygame.image.load(planetname + ".png"), (200, 200))
                            planetTouched = 1
                        elif planetTouched == "C":
                            planetname = "PSR B1257+12 b"
                            planetC = pygame.transform.scale(pygame.image.load(planetname + ".png"), (250, 250))
                            planetTouched = 2
                        elif planetTouched == "D":
                            planetname = "51 Pegasi b"
                            planetD = pygame.transform.scale(pygame.image.load(planetname + ".png"), (150, 150))
                            planetTouched = 3
                        elif planetTouched == "E":
                            planetname = "16 Cygni B b"
                            planetE = pygame.transform.scale(pygame.image.load(planetname + ".png"), (150, 150))
                            planetTouched = 4
                       
                        planetnametext = biggerfont.render(planetname, True, "#ffffff", "#090b0c")
                        planetnameRECT = planetnametext.get_rect(center=(640, 80))
                        screen.blit(planetnametext, planetnameRECT)

                        visualizationtext = font.render("Hypothetical Visualization:", True, "#ffffff", "#090b0c")
                        visualizationtextRECT = visualizationtext.get_rect(center=(640, 120))
                        screen.blit(visualizationtext, visualizationtextRECT)
                        
                        planet = pygame.transform.scale(pygame.image.load(planetname + ".png"), (500, 500))
                        screen.blit(planet, (400, 190))

                        f = open("data.txt", "w")
                        f.write(str(planetTouched))
                        f.close()

                if buttonID == 1:
                    resetScreen = True
                    f = open("data.txt", "w")
                    f.write("")
                    f.close()
        
            #Quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    # Updating the screen and setting FPS
    pygame.display.update()
    clock.tick(60)
