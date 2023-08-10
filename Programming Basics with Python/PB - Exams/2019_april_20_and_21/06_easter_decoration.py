clients = int(input())

prices = {
    "basket": 1.50,
    "wreath": 3.80,
    "chocolate bunny": 7
}

total_bill = 0

for c in range(1, clients + 1):
    items_count = 0
    client_bill = 0
    while True:
        command = input()
        if command == "Finish":
            if items_count % 2 == 0:
                client_bill *= 0.80
            print(f"You purchased {items_count} items for {client_bill:.2f} leva.")
            break
        purchase = command
        items_count += 1
        price = prices[purchase]
        client_bill += price

    total_bill += client_bill

average_bill = total_bill / clients
print(f"Average bill per client is: {average_bill:.2f} leva.")
