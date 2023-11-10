import os
import sys
import configparser
from tkinter import *
from tkinter import filedialog

import customtkinter
from pelu import main
from producciondiaria import calcularproduccion
from produccionsemanal import produccionsemanal

# ----------- Constants and Configuration ----------- #

BASE_PATH = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(BASE_PATH, 'images\INElogoPNG.ico')

# ----------- Functions ----------- #

def toggle_buttons_state(directory=None):
    state = 'normal' if directory else 'disabled'
    for btn in [button, produccion_button, produccion_semanal_button]:
        btn.configure(state=state)

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
    if selected_folder:
        save_directory_to_config(selected_folder)
        message_label.configure(text=f"Selected folder: {selected_folder}")
        toggle_buttons_state(selected_folder)

def display_output(output_func):
    for widget in root.winfo_children():
        widget.place_forget()
    directory = load_directory_from_config()
    output = output_func(directory)
    message_label.configure(text=output or "Ndaiporiveima la error")
    message_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    return_button.place(relx=0.5, rely=0.6, anchor=CENTER)

def hide_message():
    message_label.place_forget()
    return_button.place_forget()
    big_message.place(relx=0.5, rely=0.3, anchor=CENTER)
    button.place(relx=0.5, rely=0.45, anchor=CENTER)
    produccion_button.place(relx=0.5, rely=0.55, anchor=CENTER)
    directory_button.place(relx=0.5, rely=0.65, anchor=CENTER)
    produccion_semanal_button.place(relx=0.5, rely=0.75, anchor=CENTER)

# ----------- UI Initialization ----------- #

customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title("INÉ")
root.iconbitmap(ICON_PATH)
root.geometry("500x500")

big_message = customtkinter.CTkLabel(root, text="Ndetarovaonde ko herramienta ko'a", font=("Arial", 18))
big_message.place(relx=0.5, rely=0.3, anchor=CENTER)

button = customtkinter.CTkButton(root, text="Tabla de Carga", command=lambda: display_output(main))
button.place(relx=0.5, rely=0.45, anchor=CENTER)

produccion_button = customtkinter.CTkButton(root, text="Producción Diaria", command=lambda: display_output(calcularproduccion))
produccion_button.place(relx=0.5, rely=0.55, anchor=CENTER)

produccion_semanal_button = customtkinter.CTkButton(root, text="Producción Semanal", command=lambda: display_output(produccionsemanal))
produccion_semanal_button.place(relx=0.5, rely=0.75, anchor=CENTER)

message_label = customtkinter.CTkLabel(root, text="", font=("Arial", 12))
display_saved_directory()

return_button = customtkinter.CTkButton(root, text="Volver", command=hide_message)

directory_button = customtkinter.CTkButton(root, text="Escoger directorio", command=select_directory)
directory_button.place(relx=0.5, rely=0.65, anchor=CENTER)

initial_directory = load_directory_from_config()
toggle_buttons_state(initial_directory)

root.mainloop()
