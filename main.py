import customtkinter as ctk
from PIL import Image

welcomeScreen = ctk.CTk()
welcomeScreen.geometry("600x350")
welcomeScreen.resizable(False, False)
welcomeScreen.title("Project Castor")


backdrop = ctk.CTkImage(light_image=Image.open("space.jpg"),
                                  dark_image=Image.open("space.jpg"),
                                  size=(660, 371))

backdropSprite = ctk.CTkLabel(welcomeScreen, image=backdrop, text="")
backdropSprite.place(x=0, y=0)

title = ctk.CTkLabel(welcomeScreen, text="Welcome to", font=("Bungee Tint", 20))
title.place(x=70, y=100)

welcomeScreen.mainloop()