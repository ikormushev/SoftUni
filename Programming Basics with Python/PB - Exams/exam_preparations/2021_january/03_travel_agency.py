city_name = input()
package_type = input()
vip_card = input()
days = int(input())

cities_list = ["Bansko", "Borovets", "Varna", "Burgas"]
packages_list = ["noEquipment", "withEquipment", "noBreakfast", "withBreakfast"]

if city_name not in cities_list or package_type not in packages_list:
    print("Invalid input!")
elif days < 1:
    print("Days must be positive number!")
else:
    prices = {
        "withEquipment": {
            "price": 100,
            "VIP": 0.10,
        },
        "noEquipment": {
            "price": 80,
            "VIP": 0.05,
        },
        "withBreakfast": {
            "price": 130,
            "VIP": 0.12
        },
        "noBreakfast": {
            "price": 100,
            "VIP": 0.07
        }
    }

    if days > 7:
        days -= 1

    price = prices[package_type]["price"] * days

    if vip_card == "yes":
        price *= 1 - prices[package_type]["VIP"]

    print(f"The price is {price:.2f}lv! Have a nice time!")
