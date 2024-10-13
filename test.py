import pygame

pygame.init()

joystick = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

buttonPressed = ""

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            buttonID = event.button
            buttons = {
                0: "A",
                1: "B",
                2: "X",
                3: "Y",
                4: "-",
                5: "Home",
                6: "+",
                7: "Left Joystick Pressed",
                8: "Right Joystick Pressed",
                9: "L",
                10: "R",
                11: "D-Pad Up",
                12: "D-Pad Down",
                13: "D-Pad Left",
                14: "D-Pad Right",
                15: "Capture",
            }

            buttonPressed = buttons[buttonID]


            if buttonPressed == "Home":
                run = False

        elif event.type == pygame.JOYAXISMOTION:
            axis = event.axis
            value = event.value

            if axis == 0:
                if value > 0.5:
                    buttonPressed = "Left joystick moving right"
                elif value < -0.5:
                    buttonPressed = "Left joystick moving left"
            elif axis == 1:
                if value < -0.5:
                    buttonPressed = "Left joystick moving up"
                elif value > 0.5:
                    buttonPressed = "Left joystick moving down"
            

            elif axis == 2:
                if value > 0.5:
                    buttonPressed = "Right joystick moving right"
                elif value < -0.5:
                    buttonPressed = "Right joystick moving left"
            
            elif axis == 3:  # Right joystick up-down axis
                if value < -0.5:
                    buttonPressed = "Right joystick moving up"
                elif value > 0.5:
                    buttonPressed = "Right joystick moving down"

            elif axis == 4:
                if value > 0.5:
                    buttonPressed = "ZL"
            elif axis == 5:
                if value > 0.5:
                    buttonPressed = "ZR"
pygame.quit()