from tkinter import *
from pelu import main
import customtkinter
from producciondiaria import calcularproduccion
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
    button.place(relx=0.5, rely=0.45, anchor=CENTER)
    produccion_button.place(relx=0.5, rely=0.55, anchor=CENTER)
    directory_button.place(relx=0.5, rely=0.65, anchor=CENTER)


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

customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title("INÉ")
root.geometry("500x500")

# Main button
button = customtkinter.CTkButton(root, text="Tabla de Carga", command=show_message)

produccion_button = customtkinter.CTkButton(root, text="Producción Diaria", command=show_daily_production)

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
