
###
# Writes Seven Wonders of the World to a file
#

# List of the Seven Wonders of the World
seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
sorted_seven_wonders = sorted(seven_wonders)

# Write data to the file
with open(file_name, 'w') as file:
    for wonders in sorted_seven_wonders:
        file.write(wonders + "\n")

# Print confirmation
print("Seven Wonders have been saved to", file_name)
