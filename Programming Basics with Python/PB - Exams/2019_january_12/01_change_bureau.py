bitcoins_num = int(input())
yuan_num = float(input())
commission = float(input()) / 100

bitcoins_price = bitcoins_num * 1168  # BGN
yuans_price = yuan_num * 0.15  # USD
yuans_price *= 1.76  # BGN

total_price = bitcoins_price + yuans_price  # BGN
total_price = total_price / 1.95  # EUR

total_price *= 1 - commission

print(f"{total_price:.2f}")

