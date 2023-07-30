cake_width = int(input())
cake_length = int(input())

cake_area = cake_width * cake_length

while True:
    command = input()
    if command == "STOP":
        break
    pieces = int(command)
    cake_area -= pieces
    if cake_area < 0:
        break

if command == "STOP" and cake_area > 0:
    print(f"{cake_area} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_area)} pieces more.")
