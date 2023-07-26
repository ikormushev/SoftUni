campaign_days = int(input())
pasty_cooks = int(input())
cakes_num = int(input())
waffles_num = int(input())
pancakes_num = int(input())

cakes_price = cakes_num * 45
waffles_price = waffles_num * 5.80
pancakes_price = pancakes_num * 3.20

earnings_day = (cakes_price + waffles_price + pancakes_price) * pasty_cooks
earnings = earnings_day * campaign_days

earnings *= 7/8  # 1/8 of earnings is for expenses

print(f"{earnings:.2f}")
