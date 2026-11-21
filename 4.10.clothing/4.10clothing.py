# Importujemy moduł do obsługi plików CSV
import csv

# Tworzymy pustą listę na pasujące produkty
result = []

# Otwieramy plik w trybie odczytu
with open('clothing.csv', 'r') as file:

    # Tworzymy czytnik CSV
    reader = csv.reader(file)

    # Pomijamy nagłówki kolumn
    next(reader)

    # Przechodzimy po każdym produkcie
    for line in reader:

        # Pobieramy cenę i ilość z odpowiednich kolumn
        price = float(line[5])
        amount = int(line[6])

        # Sprawdzamy oba warunki
        if price < 60 and amount < 40:

            # Dodajemy pasujący produkt do listy
            result.append(line)

# Wyświetlamy znalezione produkty
print(result)