from collections import deque

seats = input().split(", ")
first_numbers = deque([int(x) for x in input().split(", ")])
second_numbers = deque([int(x) for x in input().split(", ")])

taken_seats = []
seat_matches_found = 0
rotations_count = 0

while len(taken_seats) < 3 and rotations_count < 10:
    rotations_count += 1
    first_number = first_numbers.popleft()
    second_number = second_numbers.pop()
    numbers_ascii_value = chr(first_number + second_number)

    seat_found = False
    first_seat = f"{first_number}{numbers_ascii_value}"
    second_seat = f"{second_number}{numbers_ascii_value}"
    for seat in seats:
        if (first_seat == seat or second_seat == seat) and seat not in taken_seats:
            taken_seats.append(seat)
            seat_found = True
            break

    if not seat_found:
        first_numbers.append(first_number)
        second_numbers.appendleft(second_number)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations_count}")

