def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        content = source_file.read()
        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)

copy_file("./file.txt", "./destination_file.txt")
