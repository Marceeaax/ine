import os
import datetime

def produccionsemanal(directory):
    # English to Spanish day names mapping
    day_translation = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }
    
    # Initialize totals with 0 for each day of the week in English
    totals = {english: {"viviendas": 0, "poblacion": 0} for english in day_translation.keys()}

    # Determine the current date and the Monday of the current week
    fechahoy = datetime.datetime.now().date()
    lunes_semana_actual = fechahoy - datetime.timedelta(days=fechahoy.weekday())

    # Retrieve the list of .dat files modified during the current week
    dat_files_weekday = [
        f for f in os.listdir(directory)
        if f.endswith('.dat') and lunes_semana_actual <= datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(directory, f))).date() <= fechahoy
    ]

    # Early exit if no files found
    if not dat_files_weekday:
        return ["No se encontraron archivos editados en la semana"]

    # Process files and calculate totals
    for dat_file in dat_files_weekday:
        try:
            with open(os.path.join(directory, dat_file), 'r', encoding='utf-8-sig') as file:
                for line in file:
                    if line.startswith("1"):
                        file_date = datetime.datetime.strptime(line[191:199].strip(), "%Y%m%d").date()
                        if file_date >= lunes_semana_actual:
                            weekday_name = file_date.strftime('%A')
                            totals[weekday_name]["viviendas"] += 1
                            totals[weekday_name]["poblacion"] += int(line[218:222].strip() or 0)
        except PermissionError:
            return "Emboty ra'e la nde programa"

    # Translate the English keys to Spanish
    translated_totals = {day_translation[english]: data for english, data in totals.items()}

    # Construct the result message
    messages = ["PRODUCCION SEMANAL", f"Fecha: {fechahoy}"]
    for day in day_translation.values():  # Ensure days are in order
        data = translated_totals[day]
        messages.append(f"{day}: Viviendas: {data['viviendas']}, Población: {data['poblacion']}")

    return '\n'.join(messages)

# Uncomment the following lines to test the function with a specific directory
# ruta = r'C:\censo\TM\Grabados'
# print(produccionsemanal(ruta))
