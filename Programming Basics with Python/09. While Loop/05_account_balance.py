total_money = 0

while True:
    command = input()
    if command == "NoMoreMoney":
        break
    money = float(command)
    if money < 0:
        print("Invalid operation!")
        break
    total_money += money
    print(f"Increase: {money:.2f}")

print(f"Total: {total_money:.2f}")
