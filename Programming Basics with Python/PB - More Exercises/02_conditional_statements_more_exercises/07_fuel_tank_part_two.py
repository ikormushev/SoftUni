fuel_type = input()
fuel_lt = float(input())
club_cart_ownership = input()

gasoline_lt = 2.22
diesel_lt = 2.33
gas_lt = 0.93

fuel_price = 0

if club_cart_ownership == "Yes":
    if fuel_type == "Gasoline":
        gasoline_discount = 0.18
        gasoline_lt = 2.22 - gasoline_discount
        fuel_price = fuel_lt * gasoline_lt
    elif fuel_type == "Diesel":
        diesel_discount = 0.12
        diesel_lt = 2.33 - diesel_discount
        fuel_price = fuel_lt * diesel_lt
    elif fuel_type == "Gas":
        gas_discount = 0.08
        gas_lt = 0.93 - gas_discount
        fuel_price = fuel_lt * gas_lt

elif club_cart_ownership == "No":
    if fuel_type == "Gasoline":
        fuel_price = fuel_lt * gasoline_lt
    elif fuel_type == "Diesel":
        fuel_price = fuel_lt * diesel_lt
    elif fuel_type == "Gas":
        fuel_price = fuel_lt * gas_lt

if 20 <= fuel_lt <= 25:
    discount = fuel_price * 0.08
    fuel_price = fuel_price - discount
elif fuel_lt > 25:
    discount = fuel_price * 0.10
    fuel_price = fuel_price - discount

print(f"{fuel_price:.2f} lv.")
