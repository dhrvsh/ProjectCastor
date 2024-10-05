import customtkinter as ctk
import json


app = ctk.CTk()
app.geometry("600x350")
app.resizable(False, False)
app.title("Project Castor")


with open('jsonedPlanets.json', 'r') as openfile:

	# Reading from json file
	json_object = json.load(openfile)

for i in range(100):
    print(json_object[i]["planetName"])


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = ctk.CTkComboBox(app, values=["option 1", "option 2"],
                                     command=combobox_callback)
combobox.set("option 2")

combobox.place(x=10, y=10)



app.mainloop()