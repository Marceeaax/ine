from tkinter import *
from pelu import main
import customtkinter

def show_message():
    # Hide the main button
  # Clear any existing widgets from the window
    for widget in root.winfo_children():
        widget.place_forget()

    output = main()

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


def show_daily_production():
    # Here, you can add the logic for what happens when this button is pressed
    message_label.configure(text="Producción Diaria logic not implemented yet.")
    message_label.place(relx=0.5, rely=0.3, anchor=CENTER)

customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title("INÉ")
root.geometry("500x500")

# Main button
button = customtkinter.CTkButton(root, text="Tabla de Carga", command=show_message)

produccion_button = customtkinter.CTkButton(root, text="Producción Diaria", command=show_daily_production)

# Message label
message_label = customtkinter.CTkLabel(root, text="", font=("Arial", 12))

# Return button
return_button = customtkinter.CTkButton(root, text="Return", command=hide_message)

button.place(relx=0.5, rely=0.45, anchor=CENTER)
produccion_button.place(relx=0.5, rely=0.55, anchor=CENTER)

root.mainloop()
