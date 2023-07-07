annual_fee_for_training = int(input())

price_sneakers = annual_fee_for_training - (annual_fee_for_training * 0.4)
price_outfit = price_sneakers - (price_sneakers * 0.2)
price_ball = price_outfit * 0.25
price_accessories = price_ball * 0.2

final_price = annual_fee_for_training + price_sneakers + price_outfit + price_ball + price_accessories

print(final_price)