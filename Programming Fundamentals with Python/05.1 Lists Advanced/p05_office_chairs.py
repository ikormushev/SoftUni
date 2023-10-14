rooms_num = int(input())

chairs_left = 0
not_enough_chairs = False

for i in range(1, rooms_num + 1):
    room_information = input().split(" ")
    if len(room_information[0]) < int(room_information[1]):
        needed_chairs = int(room_information[1]) - len(room_information[0])
        print(f"{needed_chairs} more chairs needed in room {i}")
        not_enough_chairs = True
        continue
    chairs_left += len(room_information[0]) - int(room_information[1])

if not not_enough_chairs:
    print(f"Game On, {chairs_left} free chairs left")
