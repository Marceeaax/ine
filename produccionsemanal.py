import os
import datetime

def produccionsemanal(directory):
    messages = []
    viviendas = poblacion = 0

    folder_path = directory

    today = datetime.datetime.now().date().weekday()

    dat_files_weekday = [
    f for f in os.listdir(folder_path)
    if f.endswith('.dat')
    and datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(folder_path, f))).date().weekday() <= today.weekday()
    ]

    if not dat_files_weekday:
        messages.append("No se encontraron archivos editados en la semana")
        return messages
    else:
        
    