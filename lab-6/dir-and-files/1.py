import os

def list_items(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    print("Directories:")
    print(directories)
    print("\nFiles:")
    print(files)
    print("\nAll items:")
    print(os.listdir(path))

list_items("./")
