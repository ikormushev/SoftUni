from math import ceil

budget = float(input())
house_area = float(input())
windows_num = int(input())
styrofoam_per_packet = float(input())
styrofoam_packet_price = float(input())

windows_area = windows_num * 2.4
house_area -= windows_area
house_area *= 1.10
styrofoam_packets_num = ceil(house_area / styrofoam_per_packet)

styrofoam_price = styrofoam_packet_price * styrofoam_packets_num

money_diff = abs(budget - styrofoam_price)


if styrofoam_price <= budget:
    print(f"Spent: {styrofoam_price:.2f}")
    print(f"Left: {money_diff:.2f}")
else:
    print(f"Need more: {money_diff:.2f}")
