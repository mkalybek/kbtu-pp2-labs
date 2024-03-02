def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

my_list = [1, 2, 3, 4, 5]
write_list_to_file("./new_file.txt", my_list)
