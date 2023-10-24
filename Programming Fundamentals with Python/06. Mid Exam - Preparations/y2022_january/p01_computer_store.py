price_without_taxes = 0
total_taxes = 0
regular_customer = False
special_customer = False

while True:
    command = input()
    if command == "regular":
        regular_customer = True
        break
    elif command == "special":
        special_customer = True
        break

    price = float(command)
    if price <= 0:
        print("Invalid price!")
        continue

    price_without_taxes += price
    total_taxes += price * 0.20

total_price = price_without_taxes + total_taxes
if special_customer:
    total_price *= 0.90

if (regular_customer or special_customer) and total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!"
          f"\nPrice without taxes: {price_without_taxes:.2f}$"
          f"\nTaxes: {total_taxes:.2f}$"
          f"\n-----------"
          f"\nTotal price: {total_price:.2f}$")
