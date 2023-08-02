page_price = float(input())
cover_price = float(input())
paper_discount = int(input()) / 100
designer_price = float(input())
money_paid_by_team = int(input()) / 100

pages = page_price * 899
covers = cover_price * 2
price = pages + covers

price *= 1 - paper_discount
price += designer_price
price *= 1 - money_paid_by_team

print(f"Avtonom should pay {price:.2f} BGN.")
