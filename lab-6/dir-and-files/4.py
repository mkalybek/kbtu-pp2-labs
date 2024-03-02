def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines in {file_path}: {len(lines)}")

count_lines("./file.txt")
