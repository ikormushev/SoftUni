money_food = float(input())
money_souvenirs = float(input())
money_hotel = float(input())

gasoline_lt_needed = (210 * 2) * 0.07
gasoline_price = gasoline_lt_needed * 1.85

money_hotel_first_day = money_hotel * 0.9
money_hotel_second_day = money_hotel * 0.85
money_hotel_third_day = money_hotel * 0.8
total_money_hotel = money_hotel_first_day + money_hotel_second_day + money_hotel_third_day

money_souvenirs_and_food = (money_food + money_souvenirs) * 3

money_needed = total_money_hotel + money_souvenirs_and_food + gasoline_price

print(f"Money needed: {money_needed:.2f}")
