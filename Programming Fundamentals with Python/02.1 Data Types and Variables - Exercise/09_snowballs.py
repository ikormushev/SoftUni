snowballs_made = int(input())

highest_snowball = {
    "weight": 0,
    "time_to_target": 0,
    "value": 0,
    "quality": 0
}

for _ in range(1, snowballs_made + 1):
    snowball_weight = int(input())
    snowball_time_to_target = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time_to_target) ** snowball_quality

    if snowball_value > highest_snowball["value"]:
        highest_snowball["weight"] = snowball_weight
        highest_snowball["time_to_target"] = snowball_time_to_target
        highest_snowball["value"] = snowball_value
        highest_snowball["quality"] = snowball_quality

print(f'{highest_snowball["weight"]} : {highest_snowball["time_to_target"]} = '
      f'{highest_snowball["value"]:.0f} ({highest_snowball["quality"]})')
