budget = float(input())

budget_left = budget
budget_not_enough = False

while True:
    command = input()
    if command == "ACTION":
        break
    actor_name = command
    if len(actor_name) <= 15:
        award = float(input())
    else:
        award = budget_left * 0.20

    budget_left -= award
    if budget_left < 0:
        budget_not_enough = True
        break

if budget_not_enough:
    print(f"We need {abs(budget_left):.2f} leva for our actors.")
else:
    print(f"We are left with {budget_left} leva.")
