groups_num = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0  # peaks - Musala, Mont Blanc, Kilimanjaro, K2, Everest
people = 0

for _ in range(1, groups_num + 1):
    people_in_group = int(input())
    if people_in_group <= 5:
        p1 += people_in_group
    elif 6 <= people_in_group <= 12:
        p2 += people_in_group
    elif 13 <= people_in_group <= 25:
        p3 += people_in_group
    elif 26 <= people_in_group <= 40:
        p4 += people_in_group
    elif people_in_group >= 41:
        p5 += people_in_group
    people += people_in_group

p1_percent = p1 / people * 100
p2_percent = p2 / people * 100
p3_percent = p3 / people * 100
p4_percent = p4 / people * 100
p5_percent = p5 / people * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")
