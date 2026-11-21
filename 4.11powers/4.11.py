# Otwieramy plik w trybie zapisu
with open('powers.txt', 'w') as file:

    # Przechodzimy przez liczby od 1 do 100
    for i in range(1, 101):

        # Obliczamy drugą i trzecią potęgę
        second_power = i ** 2
        third_power = i ** 3

        # Wyświetlamy wynik
        print(f"{i},{second_power},{third_power}")

        # Zapisujemy wynik do pliku
        file.write(f"{i},{second_power},{third_power}\n")