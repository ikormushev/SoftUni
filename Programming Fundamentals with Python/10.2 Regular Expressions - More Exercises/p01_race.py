import re

name_pattern = r"[a-zA-Z]+"
distance_pattern = r"\d"

names = input().split(", ")

racers = {}

while True:
    command = input()
    if command == "end of race":
        break
    racer_name = "".join(re.findall(name_pattern, command))
    racer_distance = re.findall(distance_pattern, command)
    distance_numbers = list(map(int, racer_distance))

    if racer_name in names:
        total_distance = sum(distance_numbers)
        if racer_name not in racers:
            racers[racer_name] = total_distance
        else:
            racers[racer_name] += total_distance

sorted_racers = dict(sorted(racers.items(), key=lambda d: -d[1]))

race_place_index = 1
for racer in sorted_racers.keys():
    race_place = ""
    if race_place_index == 1:
        race_place = "1st"
    elif race_place_index == 2:
        race_place = "2nd"
    elif race_place_index == 3:
        race_place = "3rd"
    else:
        break
    print(f"{race_place} place: {racer}")
    race_place_index += 1
