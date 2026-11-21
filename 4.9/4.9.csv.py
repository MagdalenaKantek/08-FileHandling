import csv  # module for working with CSV files

# file name
file_name = '4.9/it_company.csv'


print('GRAPHIC DESIGNERS')
print('================')

# reads CSV file
with open(file_name, 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        if row[2] == 'Graphic Designer':   # checks employee job title
            print(row[1] + ',' + row[0] + ',' + row[3])