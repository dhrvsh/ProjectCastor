import sys
import pygame
import os

pygame.init()
pygame.display.set_caption('Project Castor')
screen = pygame.display.set_mode((800, 480), 0, 32)
clock = pygame.time.Clock()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

font = pygame.font.Font("MajorMonoDisplay.ttf", 24)

# Planets data
planets = [
    {"planetName": "PSR B1257+12 c", "hostName": "PSR B1257+12", "starsNum": "1", "planetsNum": "3", "discMethod": "Pulsar Timing", "discYear": "1992", "discFacility": "Arecibo Observatory"},
    {"planetName": "PSR B1257+12 d", "hostName": "PSR B1257+12", "starsNum": "1", "planetsNum": "3", "discMethod": "Pulsar Timing", "discYear": "1992", "discFacility": "Arecibo Observatory"},
    {"planetName": "PSR B1257+12 b", "hostName": "PSR B1257+12", "starsNum": "1", "planetsNum": "3", "discMethod": "Pulsar Timing", "discYear": "1994", "discFacility": "Arecibo Observatory"},
    {"planetName": "51 Pegasi b", "hostName": "51 Peg", "starsNum": "1", "planetsNum": "1", "discMethod": "Radial Velocity", "discYear": "1995", "discFacility": "Haute-Provence Observatory"},
    {"planetName": "16 Cygni B b", "hostName": "16 Cyg B", "starsNum": "3", "planetsNum": "1", "discMethod": "Radial Velocity", "discYear": "1996", "discFacility": "Multiple Observatories"}
]

f = open("data.txt", "w")
f.write("")
f.close()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.JOYBUTTONDOWN:
            buttonID = event.button
            # if buttonID == 5:
            #     pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Clear screen with a black color
    screen.fill((0, 0, 0))

    # Open the data file and read the touched planet ID
    try:
        with open('data.txt', 'r') as dataFile:
            planetTouched = dataFile.read().strip()
    except FileNotFoundError:
        planetTouched = ""

    # If planetTouched is not empty, render the information
    if planetTouched and planetTouched.isdigit():
        planetTouchedIndex = int(planetTouched)
        
        if 0 <= planetTouchedIndex < len(planets):
            planetname = font.render("Planet Name: " + planets[planetTouchedIndex]["planetName"], True, "#ffffff", "#000000")
            hostname = font.render("Host Name: " + planets[planetTouchedIndex]["hostName"], True, "#ffffff", "#000000")
            starsnum = font.render("Number of Stars: " + planets[planetTouchedIndex]["starsNum"], True, "#ffffff", "#000000")
            planetnum = font.render("Number of Planets: " + planets[planetTouchedIndex]["planetsNum"], True, "#ffffff", "#000000")
            discmethod = font.render("Discovery Method: " + planets[planetTouchedIndex]["discMethod"], True, "#ffffff", "#000000")
            discyear = font.render("Discovery Year: " + planets[planetTouchedIndex]["discYear"], True, "#ffffff", "#000000")

            
            if planets[planetTouchedIndex]["planetName"] == "51 Pegasi b":
                discfacility = pygame.font.Font("MajorMonoDisplay.ttf", 20).render("Discovery Facility: " + planets[planetTouchedIndex]["discFacility"], True, "#ffffff", "#000000")
            else:
                discfacility = font.render("Discovery Facility: " + planets[planetTouchedIndex]["discFacility"], True, "#ffffff", "#000000")
            
            # Centering the text on the screen
            planetnameRECT = planetname.get_rect(center=(400, 80))
            hostnameRECT = hostname.get_rect(center=(400, 130))
            starsnumRECT = starsnum.get_rect(center=(400, 180))
            planetnumRECT = planetnum.get_rect(center=(400, 230))
            discmethodRECT = discmethod.get_rect(center=(400, 280))
            discyearRECT = discyear.get_rect(center=(400, 330))
            discfacilityRECT = discfacility.get_rect(center=(400, 380))
            
            # Draw all the text to the screen
            screen.blit(planetname, planetnameRECT)
            screen.blit(hostname, hostnameRECT)
            screen.blit(starsnum, starsnumRECT)
            screen.blit(planetnum, planetnumRECT)
            screen.blit(discmethod, discmethodRECT)
            screen.blit(discyear, discyearRECT)
            screen.blit(discfacility, discfacilityRECT)
    
    # Update the display
    pygame.display.update()
    clock.tick(60)
