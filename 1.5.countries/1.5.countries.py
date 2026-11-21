number = 1

with open('countries.txt', 'r') as file:  #otwiera plik do odczytu (r = read).
    for line in file:                     #pobiera kolejne linie z pliku.
        print(number, line, end="")       #wyświetla linię bez dodawania dodatkowego przejścia do nowej linii.
        number += 1
