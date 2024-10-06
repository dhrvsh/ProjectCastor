import customtkinter as ctk
from PIL import Image
import json

welcomeScreen = ctk.CTk()
welcomeScreen.geometry("600x350")
welcomeScreen.resizable(False, False)
welcomeScreen.title("Project Castor")
welcomeScreen.iconbitmap("icon.ico")

backdrop = ctk.CTkImage(light_image=Image.open("space.png"),
                                  dark_image=Image.open("space.png"),
                                  size=(600, 350))

backdropSprite = ctk.CTkLabel(welcomeScreen, image=backdrop, text="")
backdropSprite.place(x=0, y=0)


def kill():
    welcomeScreen.destroy()
    app = ctk.CTk()
    app.geometry("600x350")
    app.resizable(False, False)
    app.title("Project Castor")
    app.iconbitmap("icon.ico")

    planets = []

    with open('jsonedPlanets.json', 'r') as openfile:
        json_object = json.load(openfile)

    for i in range(100):
        planets.append(json_object[i]["planetName"])


    def getInfo():
        choice = planets.get()
        for i in range(100):
            if json_object[i]["planetName"] == choice:
                info = json_object[i]
        entry.configure(state="normal")
        entry.delete("0.0", "end")

        entry.insert("0.0", "Host Name: " + str(info["hostName"]) + "\n" +  "\n" + "Number of Stars: " + str(info["starsNu"]) + "\n" +  "\n" + "Number of Planets: " + str(info["planetsNu"]) + "\n" +  "\n" + "Discovery Method: " + str(info["discMethod"]) + "\n" +  "\n" + "Discovery Year: " + str(info["discYear"]) + "\n" +  "\n" + "Discovery Facility: " + str(info["discFacility"]) + "\n" +  "\n" + "Solution Type: " + str(info["solutionType"]))
        entry.configure(state="disabled")

    planets = ctk.CTkComboBox(app, values=planets, width=380, state="readonly")
    planets.set("Choose a planet")
    planets.place(x=35, y=30)

    getInfoButton = ctk.CTkButton(app, text="Explore the planet", command=getInfo)
    getInfoButton.place(x=420, y=29)

    entry = ctk.CTkTextbox(app, width=530, height=250, font=(None, 15))
    entry.place(x=35, y=65)
    entry.configure(state="disabled")

    app.mainloop()


enter = ctk.CTkButton(welcomeScreen, text="Start Your Journey",  font=("Bungee Tint", 15), command=kill)
enter.place(x=200, y=190)

welcomeScreen.mainloop()