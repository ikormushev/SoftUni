balls_num = int(input())

colors_num = {
    "red": 0,
    "orange": 0,
    "yellow": 0,
    "white": 0,
    "black": 0,
    "others": 0
}

color_points = {
    "red": 5,
    "orange": 10,
    "yellow": 15,
    "white": 20,
}


points = 0
black_division = 0

for _ in range(1, balls_num + 1):
    color = input()
    if color in colors_num:
        colors_num[color] += 1
    else:
        colors_num["others"] += 1

    if color in color_points:
        points += color_points[color]
    elif color == "black":
        points = points // 2
        black_division += 1
    else:
        continue

print(f"Total points: {points}")
print(f'Red balls: {colors_num["red"]}')
print(f'Orange balls: {colors_num["orange"]}')
print(f'Yellow balls: {colors_num["yellow"]}')
print(f'White balls: {colors_num["white"]}')
print(f'Other colors picked: {colors_num["others"]}')
print(f'Divides from black balls: {black_division}')
