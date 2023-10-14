electrons_num = int(input())

electron_shells = []
electrons_left = electrons_num
shell_index = 0

while electrons_left > 0:
    shell_index += 1
    maximum_electrons = 2 * (shell_index ** 2)

    if electrons_left >= maximum_electrons:
        electron_shells.append(maximum_electrons)
        electrons_left -= maximum_electrons
    else:
        electron_shells.append(electrons_left)
        electrons_left -= electrons_left

print(electron_shells)
