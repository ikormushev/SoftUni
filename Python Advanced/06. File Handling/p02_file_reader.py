import os

file_path = os.path.join("files_used", "numbers.txt")

with open(file_path, "r") as file:
    all_numbers = [int(x) for x in file.readlines()]
    numbers_sum = sum(all_numbers)
    print(numbers_sum)
