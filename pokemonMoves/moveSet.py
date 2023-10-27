import os

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return set(lines)

# Define the directory where your text files are located
directory = 'K:\Python bot\pokemonMoves\output'
file_basenames = [
    #"HealBlock",
    "stealthrock",
    "teleport"
]

# Create a dictionary to store lines and their file names
file_sets = []

# Read each file and store its lines in a set
for file_basename in file_basenames:
    file_name = file_basename + '.txt'  # Add '.txt' to the file name
    file_path = os.path.join(directory, file_name)
    file_set = read_file(file_path)
    file_sets.append(file_set)

# Find the common lines among the sets
common_lines = sorted(set.intersection(*file_sets))

# Print the common lines
for line in common_lines:
    print(line.strip())
