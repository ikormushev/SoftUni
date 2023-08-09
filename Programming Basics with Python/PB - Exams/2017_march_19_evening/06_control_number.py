first_number = int(input())
second_number = int(input())
control_number = int(input())

total_sum = 0
is_sum_greater = False
total_combinations = 0

for n1 in range(1, first_number + 1):
    for n2 in range(second_number, 0, -1):
        total_sum += (n1 * 2) + (n2 * 3)
        total_combinations += 1
        if total_sum >= control_number:
            is_sum_greater = True
            break

if is_sum_greater:
    print(f"{total_combinations} moves")
    print(f"Score: {total_sum} >= {control_number}")
else:
    print(f"{total_combinations} moves")
