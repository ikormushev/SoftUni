money_needed = float(input())
money = float(input())

days_num = 0
spending_days = 0

while True:
    action = input()
    amount = float(input())
    days_num += 1
    if action == "spend":
        spending_days += 1
        money -= amount
        if money < 0:
            money = 0
        if spending_days == 5:
            print("You can't save the money.")
            print(days_num)
            break
    elif action == "save":
        spending_days = 0
        money += amount
    if money >= money_needed:
        print(f"You saved the money for {days_num} days.")
        break
