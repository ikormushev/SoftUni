luggage_width = int(input())
luggage_height = int(input())
luggage_depth = int(input())
priority = input()

priority_fee_between_50_and_100 = {
    "true": 0,
    "false": 25
}

priority_fee_between_100_and_200 = {
    "true": 10,
    "false": 50
}

priority_fee_between_200_and_300 = {
    "true": 20,
    "false": 100
}

luggage_area = luggage_width * luggage_height * luggage_depth
fee = 0

if luggage_area <= 50:
    fee = 0
elif 50 < luggage_area <= 100:
    fee = priority_fee_between_50_and_100[priority]
elif 100 < luggage_area <= 200:
    fee = priority_fee_between_100_and_200[priority]
elif 200 < luggage_area <= 300:
    fee = priority_fee_between_200_and_300[priority]

print(f"Luggage tax: {fee:.2f}")
