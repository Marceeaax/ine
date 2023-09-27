import os
import datetime

def produccionsemanal(directory):
    messages = []
    viviendas = poblacion = 0

    folder_path = directory

    today = datetime.datetime.now().date().weekday()
    fechahoy = datetime.datetime.now().date()

    dat_files_weekday = [
    f for f in os.listdir(folder_path)
    if f.endswith('.dat')
    and datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(folder_path, f))).date().weekday() <= today
    ]

    if not dat_files_weekday:
        messages.append("No se encontraron archivos editados en la semana")
        return messages
    else:
        viviendas = poblacion = 0
        for dat_file in dat_files_weekday:
            with open(os.path.join(folder_path, dat_file), 'r', encoding='utf-8-sig') as file:
                lines = file.readlines()
                
                # line[191:199] is the date in format YYYYMMDD
                # remember that the variable today is in format YYYY-MM-DD so we need to remove the dashes in order to compare them

                for line in lines:
                    if line.startswith("1") and fechahoy == datetime.datetime.strptime(line[191:199], "%Y%m%d").date():
                        viviendas += 1
                        poblacion += int(line[218:222])

        messages.append("PRODUCCION SEMANAL")
        messages.append(f"Fecha: {fechahoy}")
        messages.append(f"Viviendas: {viviendas}")
        messages.append(f"Población: {poblacion}")
    
    return '\n'.join(messages)
