pens = int(input())
markers = int(input())
board_cleaner_lt = int(input())
discount_in_percent = int(input()) / 100

price_pens = pens * 5.8
price_markers = markers * 7.20
price_board_cleaner = board_cleaner_lt * 1.20

price_for_all = price_pens + price_markers + price_board_cleaner
final_price_with_discount = price_for_all - (price_for_all * discount_in_percent)

print(final_price_with_discount)