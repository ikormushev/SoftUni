guests_num = int(input())
guest_menu_price = float(input())
budget = float(input())

if 10 <= guests_num <= 15:
    guest_menu_price *= 0.85
elif 15 < guests_num <= 20:
    guest_menu_price *= 0.80
elif guests_num > 20:
    guest_menu_price *= 0.75

cake_price = budget * 0.10
price = guest_menu_price * guests_num
total_price = cake_price + price

money_diff = abs(budget - total_price)

if budget >= total_price:
    print(f"It is party time! {money_diff:.2f} leva left.")
else:
    print(f"No party! {money_diff:.2f} leva needed.")
