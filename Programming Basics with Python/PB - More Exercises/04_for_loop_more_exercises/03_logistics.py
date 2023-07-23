cargo_num = int(input())

microbus_c, truck_c, train_c = 0, 0, 0 # microbus_cargo, truck_cargo, train_cargo
cargo_tons_sum = 0
average_price = 0

for _ in range(1, cargo_num + 1):
    cargo_ton = int(input())
    cargo_tons_sum += cargo_ton
    if cargo_ton <= 3:
        microbus_c += cargo_ton
    elif 4 <= cargo_ton <= 11:
        truck_c += cargo_ton
    elif cargo_ton >= 12:
        train_c += cargo_ton

total_price = (microbus_c * 200) + (truck_c * 175) + (train_c * 120)
average_price = total_price / cargo_tons_sum
p1_percent = (microbus_c / cargo_tons_sum) * 100
p2_percent = (truck_c / cargo_tons_sum) * 100
p3_percent = (train_c / cargo_tons_sum) * 100

print(f"{average_price:.2f}")
print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
