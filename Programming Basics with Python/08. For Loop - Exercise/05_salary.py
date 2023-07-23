tabs_open = int(input())
salary = float(input())

fees = 0
site_fees = {
    "Facebook": 150,
    "Instagram": 100,
    "Reddit": 50
}

for _ in range(tabs_open):
    site = input()
    if site in site_fees:
        salary -= site_fees[site]
    else:
        continue
    if salary <= 0:
        print("You have lost your salary")
        break
else:
    print(f"{salary:.0f}")
