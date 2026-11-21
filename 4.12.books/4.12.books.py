# Importujemy moduł do obsługi plików CSV
import csv


# Funkcja zapisuje książkę do odpowiedniego pliku
def save_books(book_genre, book_data):

    # Sprawdzamy, czy gatunek to Fantasy
    if book_genre == 'Fantasy':
        # Otwieramy plik w trybie dopisywania
        with open('books_fantasy.txt', 'a') as file:
            # Zapisujemy dane książki
            file.write(','.join(book_data) + '\n')

    # Sprawdzamy, czy gatunek to Historical
    if book_genre == 'Historical':
        # Otwieramy plik w trybie dopisywania
        with open('books_historical.txt', 'a') as file:
            # Zapisujemy dane książki
            file.write(','.join(book_data) + '\n')

    # Sprawdzamy, czy gatunek to Romance
    if book_genre == 'Romance':
        # Otwieramy plik w trybie dopisywania
        with open('books_romance.txt', 'a') as file:
            # Zapisujemy dane książki
            file.write(','.join(book_data) + '\n')

    # Sprawdzamy, czy gatunek to Classic
    if book_genre == 'Classic':
        # Otwieramy plik w trybie dopisywania
        with open('books_classic.txt', 'a') as file:
            # Zapisujemy dane książki
            file.write(','.join(book_data) + '\n')


# Funkcja odczytuje książki z pliku CSV
def read_books():

    # Otwieramy plik do odczytu
    with open('books.csv', 'r') as file:

        # Tworzymy czytnik CSV
        reader = csv.reader(file)

        # Pomijamy nagłówki kolumn
        next(reader)

        # Przechodzimy po każdej książce
        for line in reader:

            # Pobieramy gatunek i przekazujemy dane do funkcji
            save_books(line[2], line)


# Wywołujemy funkcję odczytującą książki
read_books()