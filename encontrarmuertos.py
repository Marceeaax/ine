import os

def lines_starting_with_2(file_path):
    lines_with_2 = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        for line_num, line in enumerate(file, start=1):
            if line.startswith("2"):
                lines_with_2.append(line_num)
    return lines_with_2

def main():
    folder_path = r"C:\Users\Marcelo\Desktop\OngoingProjects\INE\INE NUEVA ERA\TM\Grabados"
    
    dat_files_with_line_starting_with_2 = {}
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.dat'):
            file_path = os.path.join(folder_path, file_name)
            lines_with_2 = lines_starting_with_2(file_path)
            if lines_with_2:
                dat_files_with_line_starting_with_2[file_name] = lines_with_2
    
    if dat_files_with_line_starting_with_2:
        print("The following .dat files contain at least one line starting with '2':")
        for dat_file, line_numbers in dat_files_with_line_starting_with_2.items():
            line_numbers_str = ', '.join(map(str, line_numbers))
            print(f"{dat_file}: Lines {line_numbers_str}")
    else:
        print("No .dat files found that contain a line starting with '2'.")

if __name__ == "__main__":
    main()
