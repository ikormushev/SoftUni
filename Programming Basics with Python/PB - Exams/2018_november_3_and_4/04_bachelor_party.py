guest_singer_price = int(input())

guest_menu_price = 0
total_earnings = 0
guests_num = 0

while True:
    command = input()
    if command == "The restaurant is full":
        break
    people_in_group = int(command)
    if people_in_group < 5:
        guest_menu_price = 100
    elif people_in_group >= 5:
        guest_menu_price = 70
    guests_price = people_in_group * guest_menu_price
    total_earnings += guests_price
    guests_num += people_in_group

if total_earnings >= guest_singer_price:
    money_left = total_earnings - guest_singer_price
    print(f"You have {guests_num} guests and {money_left} leva left.")
else:
    print(f"You have {guests_num} guests and {total_earnings} "
          f"leva income, but no singer.")
