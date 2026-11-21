###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r') as file:                   #otwieramy plik z pracownikami do odczytu.
   with open(position_file, 'w') as software_engineer:    #otwieramy plik wynikowy do zapisu.
      for line in file:                                   #przechodzimy przez każdą linię
         if job_title in line:                            #sprawdzamy, czy linia zawiera szukane stanowisko.
            software_engineer.write(line)                 #zapisujemy pasującą linię do nowego pliku.
            