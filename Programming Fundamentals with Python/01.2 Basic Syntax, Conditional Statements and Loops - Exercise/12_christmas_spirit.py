decorations_num = int(input())
days_left = int(input())

decorations = {
    "prices": {
        "Ornament Set": 2,
        "Tree Skirt": 5,
        "Tree Garland": 3,
        "Tree Lights": 15
    },
    "points": {
        "Ornament Set": 5,
        "Tree Skirt": 3,
        "Tree Garland": 10,
        "Tree Lights": 17
    }
}

total_price = 0
total_spirit = 0
is_every_third_day = False

for i in range(1, days_left + 1):
    is_every_third_day = False
    if i % 11 == 0:
        decorations_num += 2

    if i % 2 == 0:
        total_price += decorations["prices"]["Ornament Set"] * decorations_num
        total_spirit += decorations["points"]["Ornament Set"]
    if i % 3 == 0:
        is_every_third_day = True
        total_price += decorations["prices"]["Tree Skirt"] * decorations_num
        total_price += decorations["prices"]["Tree Garland"] * decorations_num

        total_spirit += decorations["points"]["Tree Skirt"]
        total_spirit += decorations["points"]["Tree Garland"]
    if i % 5 == 0:
        total_price += decorations["prices"]["Tree Lights"] * decorations_num
        total_spirit += decorations["points"]["Tree Lights"]
        if is_every_third_day:
            total_spirit += 30

    if i % 10 == 0:
        total_spirit -= 20
        total_price += decorations["prices"]["Tree Skirt"]
        total_price += decorations["prices"]["Tree Garland"]
        total_price += decorations["prices"]["Tree Lights"]

if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")
