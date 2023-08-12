hall_rent = int(input())

statuettes_price = hall_rent * 0.70
catering_price = statuettes_price * 0.85
sound_price = catering_price * 1 / 2

price = hall_rent + statuettes_price + catering_price + sound_price

print(f"{price:.2f}")
