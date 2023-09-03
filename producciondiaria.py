
import os
import datetime

def calcularproduccion():
    
    messages = []

    folder_path = "C:\\Users\\Marcelo\\Desktop\\OngoingProjects\\INE"  # Replace with the actual path to your text file
    dat_files = [f for f in os.listdir(folder_path) if f.endswith('.dat')] # List all files in the folder that end with .dat

    today = datetime.datetime.now().date()

    if not dat_files:
        messages.append("No .dat files found in the specified folder.")
        return None

    dat_files_today = [f for f in os.listdir(folder_path) 
                   if f.endswith('.dat') 
                   and datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(folder_path, f))).date() == today]

    if not dat_files_today:
        messages.append("No .dat files found for today.")
        
    
    print(today)
    print("PRODUCCION DIARIA")

calcularproduccion()