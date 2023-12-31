
import os
import datetime

def calcularproduccion(directory):
    
    messages = []
    viviendas = poblacion = 0

    folder_path = "C:\\Users\\Marcelo\\Desktop\\OngoingProjects\\INE"  # Replace with the actual path to your text file
    folder_path = directory
    dat_files = [f for f in os.listdir(folder_path) if f.endswith('.dat')] # List all files in the folder that end with .dat

    today = datetime.datetime.now().date()

    if not dat_files:
        messages.append("No se encontraron archivos .dat (que son los archivos de carga) en tu directorio seleccionado. Hi'a cheve rejavy de directorio")
        return None

    dat_files_today = [f for f in os.listdir(folder_path) 
                   if f.endswith('.dat') 
                   and datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(folder_path, f))).date() == today]

    if not dat_files_today:
        messages.append("Nderejapoiti mba'eve ko'etedia")
    else:
        viviendas = poblacion = 0
        try:
            for dat_file in dat_files_today:
                with open(os.path.join(folder_path, dat_file), 'r', encoding='utf-8-sig') as file:
                    lines = file.readlines()
                    
                    # line[191:199] is the date in format YYYYMMDD
                    # remember that the variable today is in format YYYY-MM-DD so we need to remove the dashes in order to compare them

                    for line in lines:
                        if line.startswith("1") and today == datetime.datetime.strptime(line[191:199], "%Y%m%d").date():
                            viviendas += 1
                            poblacion += int(line[218:222])
                    
            messages.append("PRODUCCION DIARIA")
            messages.append(f"Fecha: {today}")
            messages.append(f"Viviendas: {viviendas}")
            messages.append(f"Población: {poblacion}")
        except PermissionError:
                messages.append(f"Emboty ra'e na la nde programa ikatuhaguaicha acalculá la nde PRODUCCION DIARIA")


    if not messages:
        return messages.append("Hi'a cheve oiporamba la nde carga")
    else:
        return '\n'.join(messages)