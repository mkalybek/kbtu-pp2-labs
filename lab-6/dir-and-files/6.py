import string

for letter in string.ascii_uppercase:
    file_name = f"./alphabet/{letter}.txt"
    with open(file_name, 'w') as file:
        file.write(f"This is file {letter}.txt content.")
