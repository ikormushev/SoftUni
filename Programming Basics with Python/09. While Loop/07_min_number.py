from sys import maxsize

min_number = maxsize
data = input()
while data != "Stop":
    new_number = int(data)
    if new_number <= min_number:
        min_number = new_number
    data = input()

print(min_number)
