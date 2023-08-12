from math import floor, ceil

tennis_racket_price = float(input())
tennis_rackets_num = int(input())
shoes_num = int(input())

shoes_price = tennis_racket_price * 1/6
shoes = shoes_price * shoes_num

tennis_rackets = tennis_rackets_num * tennis_racket_price
others = (tennis_rackets + shoes) * 0.20

total_price = shoes + tennis_rackets + others

price_paid_by_player = total_price * 1/8
price_paid_by_sponsors = total_price * 7/8

print(f"Price to be paid by Djokovic {floor(price_paid_by_player)}")
print(f"Price to be paid by sponsors {ceil(price_paid_by_sponsors)}")
