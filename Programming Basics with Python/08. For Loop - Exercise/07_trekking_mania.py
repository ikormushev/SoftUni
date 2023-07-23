groups_num = int(input())

people_num = 0
h1, h2, h3, h4, h5 = 0, 0, 0, 0, 0

for _ in range(1, groups_num + 1):
    people_in_group = int(input())
    people_num += people_in_group
    if people_in_group <= 5:
        h1 += people_in_group
    elif 6 <= people_in_group <= 12:
        h2 += people_in_group
    elif 13 <= people_in_group <= 25:
        h3 += people_in_group
    elif 26 <= people_in_group <= 40:
        h4 += people_in_group
    elif people_in_group >= 41:
        h5 += people_in_group

h1_percent = h1 / people_num * 100
h2_percent = h2 / people_num * 100
h3_percent = h3 / people_num * 100
h4_percent = h4 / people_num * 100
h5_percent = h5 / people_num * 100

print(f"{h1_percent:.2f}%")
print(f"{h2_percent:.2f}%")
print(f"{h3_percent:.2f}%")
print(f"{h4_percent:.2f}%")
print(f"{h5_percent:.2f}%")
