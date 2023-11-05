dwarfs = {}
seen_colors = {}

while True:
    command = input()
    if command == "Once upon a time":
        break
    dwarf_info = command.split(" <:> ")
    dwarf_name, dwarf_hat_color, dwarf_physics = dwarf_info[0], dwarf_info[1], int(dwarf_info[2])
    dwarf_with_color = dwarf_name + ">" + dwarf_hat_color

    if dwarf_with_color not in dwarfs:
        dwarfs[dwarf_with_color] = dwarf_physics
        if dwarf_hat_color not in seen_colors:
            seen_colors[dwarf_hat_color] = 1
        else:
            seen_colors[dwarf_hat_color] += 1
    else:
        if dwarf_physics > dwarfs[dwarf_with_color]:
            dwarfs[dwarf_with_color] = dwarf_physics

dwarfs = dict(sorted(dwarfs.items(), key=lambda d: (-d[1], -seen_colors[(d[0].split(">"))[1]])))

for (dwarf, physics) in dwarfs.items():
    wanted_dwarf = dwarf.split(">")
    print(f"({wanted_dwarf[1]}) {wanted_dwarf[0]} <-> {physics}")
