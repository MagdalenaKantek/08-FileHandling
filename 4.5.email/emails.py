
import re  # Importujemy moduł do pracy z wyrażeniami regularnymi


# Funkcja pobiera adres email nadawcy
def email_sender(file_name):

    # Otwieramy plik w trybie odczytu
    with open(file_name, 'r') as file:

        # Odczytujemy całą zawartość pliku jako tekst
        content = file.read()

    # Przechodzimy po każdej linijce tekstu
    for line in content.splitlines():

        # Sprawdzamy, czy linijka zawiera informację o nadawcy
        if 'From:' in line:

            # Wzorzec wyszukujący tekst znajdujący się między < i >
            pattern = '<[^>]+>'

            # Wyszukujemy adres email pasujący do wzorca
            sender = re.findall(pattern, line)

            # Usuwamy znaki < i > z odnalezionego adresu
            sender = sender[0].replace('<', '').replace('>', '')

            # Zwracamy adres email nadawcy
            return sender


# Funkcja pobiera adres email odbiorcy
def email_recipient(file_name):

    # Otwieramy plik w trybie odczytu
    with open(file_name, 'r') as file:

        # Odczytujemy całą zawartość pliku
        content = file.read()

    # Przechodzimy po każdej linijce tekstu
    for line in content.splitlines():

        # Sprawdzamy, czy linijka zawiera informację o odbiorcy
        if 'To:' in line:

            # Wzorzec wyszukujący tekst znajdujący się między < i >
            pattern = '<[^>]+>'

            # Wyszukujemy adres email pasujący do wzorca
            recipient = re.findall(pattern, line)

            # Usuwamy znaki < i > z odnalezionego adresu
            recipient = recipient[0].replace('<', '').replace('>', '')

            # Zwracamy adres email odbiorcy
            return recipient


# Funkcja pobiera temat wiadomości email
def email_subject(file_name):

    # Otwieramy plik w trybie odczytu
    with open(file_name, 'r') as file:

        # Odczytujemy całą zawartość pliku
        content = file.read()

    # Przechodzimy po każdej linijce tekstu
    for line in content.splitlines():

        # Sprawdzamy, czy linijka zawiera temat wiadomości
        if 'Subject:' in line:

            # Wzorzec wyszukujący tekst znajdujący się po Subject:
            pattern = 'Subject: .*'

            # Wyszukujemy temat wiadomości
            subject = re.findall(pattern, line)

            # Usuwamy napis Subject: i pozostawiamy sam temat
            subject = subject[0].replace('Subject: ', '')

            # Zwracamy temat wiadomości
            return subject


# Funkcja pobiera treść wiadomości email
def email_body(file_name):

    # Otwieramy plik w trybie odczytu
    with open(file_name, 'r') as file:

        # Odczytujemy całą zawartość pliku
        content = file.read()

    # Dzielimy tekst w miejscu dwóch pustych linii
    # Element [1] oznacza, że pobieramy część po nagłówkach
    body = content.split('\n\n')[1]

    # Zwracamy treść wiadomości
    return body
