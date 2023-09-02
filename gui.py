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
    button.place(relx=0.5, rely=0.5, anchor=CENTER)


customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title("INÉ")
root.geometry("500x500")

# Main button
button = customtkinter.CTkButton(root, text="Tabla de Carga", command=show_message)

# Message label
message_label = customtkinter.CTkLabel(root, text="", font=("Arial", 12))

# Return button
return_button = customtkinter.CTkButton(root, text="Return", command=hide_message)

button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
