file_name = "4.8/files.txt"

with open(file_name, 'r') as file:
    content = file.read()

file_lines = content.splitlines()

for line in file_lines:
    extension = line.split('.')[1]  # Gets file extension
    
    if len(extension) == 4:
        print(line)      # Prints only files with 4-character extensions