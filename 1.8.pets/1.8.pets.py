def read_from_file(name):
    with open('pets.txt') as file:
        content = file.read()
    return content

text = read_from_file('pets.txt')

words = text.split()

number_of_words = len(words)

print(text)
print('Number of words:', number_of_words)