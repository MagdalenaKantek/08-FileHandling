import re  # module for regular expressions

# reads text entered by the user
text = input('Enter text: ')

pattern = '[aeiouAEIOU]'  # pattern for vowels

vowels = re.findall(pattern, text)  # Finds all vowels in the text

number_of_vowels = len(vowels)  # Counts vowels

print('Number of vowels:', number_of_vowels)  # Prints the result