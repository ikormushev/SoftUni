spacecraft_width = float(input())
spacecraft_length = float(input())
spacecraft_height = float(input())
astronauts_average_height = float(input())

spacecraft_area = spacecraft_width * spacecraft_length * spacecraft_height
astronaut_room_area = 2 * 2 * (astronauts_average_height + 0.40)

astronauts_num = spacecraft_area // astronaut_room_area

if astronauts_num < 3:
    print("The spacecraft is too small.")
elif 3 <= astronauts_num <= 10:
    print(f"The spacecraft holds {astronauts_num:.0f} astronauts.")
else:
    print("The spacecraft is too big.")
