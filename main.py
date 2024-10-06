import customtkinter as ctk
from PIL import Image

welcomeScreen = ctk.CTk()
welcomeScreen.geometry("600x350")
welcomeScreen.resizable(False, False)
welcomeScreen.title("Project Castor")

def kill():
    welcomeScreen.withdraw()

backdrop = ctk.CTkImage(light_image=Image.open("space.jpg"),
                                  dark_image=Image.open("space.png"),
                                  size=(600, 350))

backdropSprite = ctk.CTkLabel(welcomeScreen, image=backdrop, text="")
backdropSprite.place(x=0, y=0)



enter = ctk.CTkButton(welcomeScreen, text="Start Your Journey",  font=("Bungee Tint", 15), command=kill)
enter.place(x=200, y=190)

welcomeScreen.mainloop()