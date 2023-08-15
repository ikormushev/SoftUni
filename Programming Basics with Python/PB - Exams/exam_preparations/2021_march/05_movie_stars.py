actors_budget = float(input())

budget_left = actors_budget

while True:
    command = input()
    if command == "ACTION":
        break
    actor_name = command

    if len(actor_name) <= 15:
        money_reward = float(input())
    else:
        money_reward = budget_left * 0.20

    budget_left -= money_reward
    if budget_left <= 0:
        break

if budget_left >= 0:
    print(f"We are left with {budget_left:.2f} leva.")
else:
    print(f"We need {abs(budget_left):.2f} leva for our actors.")
