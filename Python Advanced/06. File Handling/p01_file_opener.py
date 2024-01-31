import os

file_path = os.path.join("files_used", "text.txt")

try:
    file = open(file_path)
    print("File found")
    file.close()
except FileNotFoundError:
    print("File not found")
