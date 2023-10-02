import os
import sys

from tkinter import *
from pelu import main
import customtkinter
from producciondiaria import calcularproduccion
from produccionsemanal import produccionsemanal
from tkinter import filedialog
import configparser


def save_directory_to_config(directory):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'directory': directory}
    with open('app_config.ini', 'w') as configfile:
        config.write(configfile)

def load_directory_from_config():
    config = configparser.ConfigParser()
    config.read('app_config.ini')
    return config['DEFAULT'].get('directory', None)

def display_saved_directory():
    directory = load_directory_from_config()
    if directory:
        message_label.configure(text=f"Last selected folder: {directory}")

def select_directory():
    selected_folder = filedialog.askdirectory(title="Select a Folder")
    if selected_folder:  # Ensure a folder was selected
        # Here, you can process the selected folder as required
        save_directory_to_config(selected_folder)
        message_label.configure(text=f"Selected folder: {selected_folder}")

def show_message():
    # Hide the main button
  # Clear any existing widgets from the window
    for widget in root.winfo_children():
        widget.place_forget()

    directory = load_directory_from_config()

    output = main(directory)

    ## if output is empty, show a message

    if not output:
        output = "Ndaiporiveima la error"

    message_label.configure(text="")

    # Show the message
    message_label.configure(text=output)
    message_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    # Show the return button
    return_button.place(relx=0.5, rely=0.6, anchor=CENTER)

def hide_message():
    # Hide the message and the return button
    message_label.place_forget()
    return_button.place_forget()

    # Show the main button again
    big_message.place(relx=0.5, rely=0.3, anchor=CENTER)
    button.place(relx=0.5, rely=0.45, anchor=CENTER)
    produccion_button.place(relx=0.5, rely=0.55, anchor=CENTER)
    directory_button.place(relx=0.5, rely=0.65, anchor=CENTER)
    produccion_semanal_button.place(relx=0.5, rely=0.75, anchor=CENTER)


def show_daily_production():
    # Here, you can add the logic for what happens when this button is pressed
    for widget in root.winfo_children():
        widget.place_forget()

    directory = load_directory_from_config()
    output = calcularproduccion(directory)

    message_label.configure(text="")
    message_label.configure(text=output)
    message_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    return_button.place(relx=0.5, rely=0.6, anchor=CENTER)

def show_weekly_production():
    for widget in root.winfo_children():
        widget.place_forget()

    directory = load_directory_from_config()
    output = produccionsemanal(directory)

    message_label.configure(text="")
    message_label.configure(text=output)
    message_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    return_button.place(relx=0.5, rely=0.6, anchor=CENTER)

# inicio importar icono 

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle/exe
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

# Set the icon path accordingly
icon_path = os.path.join(base_path, 'images\INElogoPNG.ico')
print("Icon path:", icon_path)
# opa upepe


customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title("INÉ")
root.iconbitmap(icon_path)
root.geometry("500x500")

big_message = customtkinter.CTkLabel(root, text="Ndetarovaonde ko herramienta ko'a", font=("Arial", 18))
big_message.place(relx=0.5, rely=0.3, anchor=CENTER)

# Main button
button = customtkinter.CTkButton(root, text="Tabla de Carga", command=show_message)

produccion_button = customtkinter.CTkButton(root, text="Producción Diaria", command=show_daily_production)

produccion_semanal_button = customtkinter.CTkButton(root, text="Producción Semanal", command=show_weekly_production)
produccion_semanal_button.place(relx=0.5, rely=0.75, anchor=CENTER)  # Adjust the position as needed

# Message label
message_label = customtkinter.CTkLabel(root, text="", font=("Arial", 12))

display_saved_directory()

# Return button
return_button = customtkinter.CTkButton(root, text="Volver", command=hide_message)


button.place(relx=0.5, rely=0.45, anchor=CENTER)
produccion_button.place(relx=0.5, rely=0.55, anchor=CENTER)

directory_button = customtkinter.CTkButton(root, text="Escoger directorio", command=select_directory)
directory_button.place(relx=0.5, rely=0.65, anchor=CENTER)  # You can adjust the positioning as needed


root.mainloop()
