last_sector = input()
first_sector_rows = int(input())
seats_odd_row = int(input())

sector_rows = first_sector_rows
total_seats = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, sector_rows + 1):
        if row % 2 == 0:
            for s1 in range(ord("a"), ord("a") + seats_odd_row + 2):
                print(f"{chr(sector)}{row}{chr(s1)}")
                total_seats += 1
        else:
            for s2 in range(ord("a"), ord("a") + seats_odd_row):
                print(f"{chr(sector)}{row}{chr(s2)}")
                total_seats += 1
    sector_rows += 1
print(total_seats)
