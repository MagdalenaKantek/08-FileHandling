###
# Oblicza całkowitą kwotę wydaną na zakupy
#

import re  # Import modułu do wyrażeń regularnych

# Nazwa pliku z raportem zakupów
email_file = 'report.txt'


# Odczytanie zawartości pliku
def e_mail(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        email = file.read()
    return email


# Wywołanie funkcji i zapisanie zawartości pliku
email = e_mail(email_file)


# Wzorzec wyrażenia regularnego wyszukujący kwoty
pattern = '€[0-9]+'


# Wyszukanie wszystkich kwot w tekście
amounts = re.findall(pattern, email)


# Obliczenie sumy wszystkich zakupów
total = 0

for amount in amounts:
    amount = amount.replace("€", "")  # Usunięcie symbolu euro
    amount = int(amount)              # Zamiana tekstu na liczbę
    total += amount                   # Dodanie kwoty do sumy


# Wyświetlenie wyniku
print(total)