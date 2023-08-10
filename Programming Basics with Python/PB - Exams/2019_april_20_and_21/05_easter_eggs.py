eggs_painted = int(input())

eggs = {
    "red": 0,
    "orange": 0,
    "blue": 0,
    "green": 0
}
max_eggs_color = ""
max_eggs_num = 0

for e in range(1, eggs_painted + 1):
    egg_color = input()
    eggs[egg_color] += 1
    if eggs[egg_color] > max_eggs_num:
        max_eggs_num = eggs[egg_color]
        max_eggs_color = egg_color

print(f'Red eggs: {eggs["red"]}')
print(f'Orange eggs: {eggs["orange"]}')
print(f'Blue eggs: {eggs["blue"]}')
print(f'Green eggs: {eggs["green"]}')
print(f"Max eggs: {max_eggs_num} -> {max_eggs_color}")
