file_name = input('File name: ')   #Plik który wprowadza użytkownik.


try:    #Próbujemy otworzyc plik
    with open(file_name, 'r') as file:
        content = file.read()
        lines = content.splitlines()  # Divides text into lines
        words = content.split()  # Divides text into words
        print('Number of lines:', len(lines))
        print('Number of chatracters:', len(content))
        print('Number of words:', len(words))  # Counts words

except FileNotFoundError:
    print("File not found!")

#4.6/books.csv
#4.6/email.txt
#4.6/Sherlock.txt