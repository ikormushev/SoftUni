groups_num = int(input())

hills = {"Musala": 0, "Mont Blanc": 0, "Kilimanjaro": 0, "K2": 0, "Everest": 0}

hikers_total = 0

for _ in range(1, groups_num + 1):
    people_in_group = int(input())
    if people_in_group <= 5:
        hills["Musala"] += people_in_group
    elif 6 <= people_in_group <= 12:
        hills["Mont Blanc"] += people_in_group
    elif 13 <= people_in_group <= 25:
        hills["Kilimanjaro"] += people_in_group
    elif 26 <= people_in_group <= 40:
        hills["K2"] += people_in_group
    else:
        hills["Everest"] += people_in_group
    hikers_total += people_in_group

print(f'{(hills["Musala"] / hikers_total * 100):.2f}%')
print(f'{(hills["Mont Blanc"] / hikers_total * 100):.2f}%')
print(f'{(hills["Kilimanjaro"] / hikers_total * 100):.2f}%')
print(f'{(hills["K2"] / hikers_total * 100):.2f}%')
print(f'{(hills["Everest"] / hikers_total * 100):.2f}%')
