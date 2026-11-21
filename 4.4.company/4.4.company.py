counter = 0

with open('it_company.csv', 'r') as file:
    for line in file:
        print(line, end='')
        counter += 1

        if counter == 5:
            input('\nPress Enter key...')
            counter = 0