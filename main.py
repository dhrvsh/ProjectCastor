import customtkinter as ctk
from PIL import Image

app = ctk.CTk()
app.geometry("600x350")
app.resizable(False, False)
app.title("Project Castor")


backdrop = ctk.CTkImage(light_image=Image.open("space.jpg"),
                                  dark_image=Image.open("space.jpg"),
                                  size=(660, 371))

backdropSprite = ctk.CTkLabel(app, image=backdrop, text="")
backdropSprite.place(x=0, y=0)

title = ctk.

app.mainloop()