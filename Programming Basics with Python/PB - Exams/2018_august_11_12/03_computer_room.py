month = input()
hours_in_room = int(input())
people_in_group = int(input())
time_of_day = input()

price = 0

if month in ["march", "april", "may"]:
    if time_of_day == "day":
        price = 10.50
    elif time_of_day == "night":
        price = 8.4
elif month in ["june", "july", "august"]:
    if time_of_day == "day":
        price = 12.60
    elif time_of_day == "night":
        price = 10.20

if people_in_group >= 4:
    price *= 0.90
if hours_in_room >= 5:
    price *= 0.5

total_price = price * people_in_group * hours_in_room
print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")
