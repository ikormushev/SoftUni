city_name = input()
packet_type = input()
vip_discount = input()
days = int(input())

cities_list = ["Bansko", "Borovets", "Varna", "Burgas"]
packets_list = ["noEquipment", "withEquipment", "noBreakfast", "withBreakfast"]

daily_prices = {
    "withEquipment": {
        "Bansko": 100,
        "Borovets": 100,
        "vip_discount": {
            "yes": 0.10,
            "no": 0
        }
    },
    "noEquipment": {
        "Bansko": 80,
        "Borovets": 80,
        "vip_discount": {
            "yes": 0.05,
            "no": 0
        }
    },
    "withBreakfast": {
        "Varna": 130,
        "Burgas": 130,
        "vip_discount": {
            "yes": 0.12,
            "no": 0
        }
    },
    "noBreakfast": {
        "Varna": 100,
        "Burgas": 100,
        "vip_discount": {
            "yes": 0.07,
            "no": 0
        }
    }
}

if days > 7:
    days -= 1
if city_name not in cities_list or packet_type not in packets_list:
    print(f"Invalid input!")
else:
    if days < 1:
        print("Days must be positive number!")
    else:
        price = daily_prices[packet_type][city_name] * days
        price *= 1 - daily_prices[packet_type]["vip_discount"][vip_discount]

        print(f"The price is {price:.2f}lv! Have a nice time!")
