import customtkinter as ctk
import json


app = ctk.CTk()
app.geometry("600x350")
app.resizable(False, False)
app.title("Project Castor")

planets = []

with open('jsonedPlanets.json', 'r') as openfile:

	# Reading from json file
	json_object = json.load(openfile)

for i in range(100):
    planets.append(json_object[i]["planetName"])

def combobox_callback(choice):
    for i in range(100):
        if json_object[i]["planetName"] == choice:
            print(json_object[i])

combobox = ctk.CTkComboBox(app, values=planets, command=combobox_callback, state="readonly")
combobox.set("Choose a planet")
combobox.place(x=10, y=10)

combobox["state"] = "disabled"

app.mainloop()