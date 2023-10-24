initial_energy = int(input())

battles_won = 0
energy_left = initial_energy

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {battles_won}. Energy left: {energy_left}")
        break

    energy = int(command)
    if energy_left - energy >= 0:
        battles_won += 1
        energy_left -= energy
        if battles_won % 3 == 0:
            energy_left += battles_won
    else:
        print(f"Not enough energy! "
              f"Game ends with {battles_won} won battles and {energy_left} energy")
        break

