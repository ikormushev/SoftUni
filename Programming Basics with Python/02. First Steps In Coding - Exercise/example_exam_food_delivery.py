number_chicken_menus = int(input())
number_fish_menus = int(input())
number_veggie_menus = int(input())

price_chicken_menu = number_chicken_menus * 10.35
price_fish_menus = number_fish_menus * 12.4
price_veggie_menus = number_veggie_menus * 8.15

price_menus = price_chicken_menu + price_fish_menus + price_veggie_menus
price_dessert = price_menus * 0.2

final_price = price_menus + price_dessert + 2.5

print(final_price)