from collections import deque

elves_energy = deque([int(x) for x in input().split()])
materials_per_box = [int(x) for x in input().split()]

total_energy_used = 0
total_toys = 0
elves_count = 0

while elves_energy and materials_per_box:
    elf_energy = elves_energy.popleft()
    materials = materials_per_box.pop()
    if elf_energy < 5:
        materials_per_box.append(materials)
        continue
    elves_count += 1
    toy_created = False
    if elf_energy >= materials:
        toys_created = 0
        if elves_count % 3 == 0:
            if elf_energy >= materials * 2:
                toy_created = True
                toys_created = 2

                total_energy_used += materials * 2
                elf_energy -= materials * 2
            else:
                elf_energy *= 2
                elves_energy.append(elf_energy)
                materials_per_box.append(materials)
        else:
            toy_created = True
            toys_created = 1

            total_energy_used += materials
            elf_energy -= materials

        total_toys += toys_created

        if elves_count % 5 == 0:
            total_toys -= toys_created
            elves_energy.append(elf_energy)
        elif toy_created:
            elf_energy += 1
            elves_energy.append(elf_energy)
    else:
        elf_energy *= 2
        elves_energy.append(elf_energy)
        materials_per_box.append(materials)

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy_used}")

if elves_energy:
    print(f"Elves left:", end=" ")
    print(*elves_energy, sep=", ")

if materials_per_box:
    print(f"Boxes left:", end=" ")
    print(*materials_per_box, sep=", ")
