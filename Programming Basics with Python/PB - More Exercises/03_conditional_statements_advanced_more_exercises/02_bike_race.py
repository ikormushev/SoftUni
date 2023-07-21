juniors_num = int(input())
seniors_num = int(input())
route_type = input()

bikers_num = juniors_num + seniors_num
money = 0

if route_type == "trail":
    money = juniors_num * 5.50 + seniors_num * 7
if route_type == "cross-country":
    money = juniors_num * 8 + seniors_num * 9.50
    if bikers_num >= 50:
        money = money * 0.75
if route_type == "downhill":
    money = juniors_num * 12.25 + seniors_num * 13.75
if route_type == "road":
    money = juniors_num * 20 + seniors_num * 21.50

expenses = money * 0.05

money -= expenses

print(f"{money:.2f}")
