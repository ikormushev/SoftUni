break_time = int(input())
computer_part_price = float(input())
program_price = float(input())
white_frappe_price = float(input())

break_time_without_frappe = break_time - 5
shopping_time_computer_part = 3 * 2
shopping_time_program = 2 * 2
relax_time = break_time_without_frappe - shopping_time_computer_part - shopping_time_program

computer_part = computer_part_price * 3
program = program_price * 2

final_price = computer_part + program + white_frappe_price

print(f"{final_price:.2f}")
print(relax_time)
