budget = float(input())
series_num = int(input())

series_list = ["Thrones", "Lucifer", "Protector", "TotalDrama", "Area"]

some_series_discount = {
    "Thrones": 0.50,
    "Lucifer": 0.40,
    "Protector": 0.30,
    "TotalDrama": 0.20,
    "Area": 0.10
}

budget_left = budget

for _ in range(1, series_num + 1):
    series_name = input()
    series_price = float(input())
    if series_name in series_list:
        series_price *= 1 - some_series_discount[series_name]
    budget_left -= series_price

if budget_left >= 0:
    print(f"You bought all the series and left with {budget_left:.2f} lv.")
else:
    print(f"You need {abs(budget_left):.2f} lv. more to buy the series!")
