from sys import maxsize

max_number = -maxsize
while True:
    data = input()
    if data == "Stop":
        break
    new_number = int(data)
    if new_number >= max_number:
        max_number = new_number

print(max_number)
