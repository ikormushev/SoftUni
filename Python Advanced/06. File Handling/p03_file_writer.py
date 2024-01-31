import os

file_path = os.path.join("files_used", "my_first_file.txt")

with open(file_path, "w") as file:
    file.write("I just created my first file!")
