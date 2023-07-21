season = input()
group_type = input()
students_num = int(input())
nights_num = int(input())

price = 0
discount = 0
sport = ""

if season == "Winter":
    if group_type == "boys":
        price = students_num * 9.60 * nights_num
        sport = "Judo"
    elif group_type == "girls":
        price = students_num * 9.60 * nights_num
        sport = "Gymnastics"
    elif group_type == "mixed":
        price = students_num * 10 * nights_num
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys":
        price = students_num * 7.20 * nights_num
        sport = "Tennis"
    elif group_type == "girls":
        price = students_num * 7.20 * nights_num
        sport = "Athletics"
    elif group_type == "mixed":
        price = students_num * 9.50 * nights_num
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        price = students_num * 15 * nights_num
        sport = "Football"
    elif group_type == "girls":
        price = students_num * 15 * nights_num
        sport = "Volleyball"
    elif group_type == "mixed":
        price = students_num * 20 * nights_num
        sport = "Swimming"

if students_num >= 50:
    discount = price * 0.50
elif 20 <= students_num < 50:
    discount = price * 0.15
elif 10 <= students_num < 20:
    discount = price * 0.05

price -= discount

print(f"{sport} {price:.2f} lv.")
