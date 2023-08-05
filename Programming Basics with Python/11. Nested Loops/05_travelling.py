savings = 0

while True:
    command = input()
    if command == "End":
        break
    destination = command
    budget_min = float(input())
    while True:
        earnings = float(input())
        savings += earnings
        if savings >= budget_min:
            print(f"Going to {destination}!")
            savings = 0
            break
