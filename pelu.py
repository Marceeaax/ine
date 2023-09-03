from dataclasses import dataclass
import os

messages = []

def get_latest_dat_file(folder_path):
    dat_files = [f for f in os.listdir(folder_path) if f.endswith('.dat')] # List all files in the folder that end with .dat
    
    if not dat_files:
        messages.append("No .dat files found in the specified folder.")
        return None
    
    latest_file = max(dat_files, key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))
    return os.path.join(folder_path, latest_file)

def imprimircuestionario(ae, identificadorvivienda):
    messages.append(f"AE: {ae}")
    messages.append(f"Identificador vivienda: {identificadorvivienda}")

"""@dataclass
class Cuestionario:
    AE: str
    poblaciondigitada: str
    habitantes: str
    cantidadhombres: str
    cantidadmujeres: str
    fecundidad: str
    identificadorvivienda: str
    ordenvivienda: str"""

"""viviendas = []"""

def main():

    messages.clear()

    folder_path = "C:\\Users\\Marcelo\\Desktop\\OngoingProjects\\INE"  # Replace with the actual path to your text file
    file_path = get_latest_dat_file(folder_path)
    numeroviviendas = 0
    mujeresdigitadas = 0
    hombresdigitados = 0
    singenero = 0

    ae = 0
    poblaciondigitada = 0
    habitantes = 0
    cantidadhombres = 0
    cantidadmujeres = 0
    fecundidad = 0
    identificadorvivienda = 0
    ordenvivienda = 0

    try:
        # Read all lines from the text file and store them in a list
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            lines = file.readlines()

            # Check if the first line needs special handling
            if lines[0].startswith("ï"):
                if len(lines[0]) >= 2 and lines[0][1] == "1":
                    characters_166_and_167 = lines[0][165:167]
                    #messages.append(f"166th and 167th characters: {characters_166_and_167}")
            
            # Count lines that start with the number 1
            for line in lines:
                if line.startswith("1"):
                    numeroviviendas += 1
                    #messages.append(f"AE: {line[13:15]}")
                    ae = line[13:15]
                    if(int(ae) > 5):
                        messages.append("AE mayor a 5")
                    #messages.append(f"Identificador vivienda: {line[20:23]}")
                    identificadorvivienda = line[20:23]
                    #messages.append(f"Orden vivienda: {line[23:25]}")
                    ordenvivienda = line[23:25]
                    #messages.append(f"Poblacion nominal: {line[165:167]}")
                    poblacionnominal = line[165:167]
                    #messages.append(f"Hombres: {line[167:169]}")
                    hombres = line[167:169]
                    #messages.append(f"Mujeres: {line[169:171]}")
                    mujeres = line[169:171]
                    #messages.append(f"Poblacion digitada: {line[218:222]}")
                    poblaciondigitada = line[218:222]

                    if(poblacionnominal != "  "):
                        if(int(poblacionnominal) > int(poblaciondigitada)):
                            imprimircuestionario(ae, identificadorvivienda)
                            messages.append("Poblacion nominal mayor a poblacion digitada")
                        elif (int(poblacionnominal) < int(poblaciondigitada)):
                            imprimircuestionario(ae, identificadorvivienda)
                            messages.append("Poblacion nominal menor a poblacion digitada")
                        
                else:
                    if line.startswith("6"):
                        genero = line[80:81]
                        match genero:
                            case "1":
                                hombresdigitados += 1
                            case "6":
                                mujeresdigitadas += 1
                            case _:
                                singenero += 1
                    else:
                        if line.startswith("7"):
                        #imprimir hombres y mujeres digitados
                        #messages.append(f"Hombres digitados: {hombresdigitados}")
                        #messages.append(f"Mujeres digitadas: {mujeresdigitadas}")

                            if(hombres != "  "):
                                if(hombresdigitados != int(hombres)):
                                    imprimircuestionario(ae, identificadorvivienda)
                                    messages.append("Hombres digitados no coinciden con hombres")
                                    messages.append(f"Hombres digitados: {hombresdigitados}")
                                    messages.append(f"Hombres listados: {hombres}")

                            if(mujeres != "  "):
                                if(mujeresdigitadas != int(mujeres)):
                                    imprimircuestionario(ae, identificadorvivienda)
                                    messages.append("Mujeres digitadas no coinciden con mujeres")
                                    messages.append(f"Mujeres digitadas: {mujeresdigitadas}")
                                    messages.append(f"Mujeres listadas: {mujeres}")
                            
                            hombresdigitados = mujeresdigitadas = singenero = 0

            #messages.append(f"Number of lines starting with 1: {numeroviviendas}")
    except FileNotFoundError:
        messages.append("The file could not be found.")
    except IOError as e:
        messages.append(f"An error occurred while reading the file: {e}")

    return '\n'.join(messages)

if __name__ == "__main__":
    main()
