last_sector = input()
rows_sector_one = int(input())
seats_odd_row = int(input())

starting_rows = rows_sector_one
seats_total = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, starting_rows + 1):
        seat_odd_name = ord("a")
        seat_even_name = ord("a")
        if row % 2 == 1:
            for seat_odd_num in range(1, seats_odd_row + 1):
                seats_total += 1
                print(f"{chr(sector)}{row}{chr(seat_odd_name)}")
                seat_odd_name += 1
        else:
            for seat_even_num in range(1, (seats_odd_row + 2) + 1):
                seats_total += 1
                print(f"{chr(sector)}{row}{chr(seat_even_name)}")
                seat_even_name += 1
    starting_rows += 1
print(seats_total)
