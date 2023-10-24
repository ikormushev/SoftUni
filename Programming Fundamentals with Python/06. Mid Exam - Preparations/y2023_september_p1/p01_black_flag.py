def plunder(days, each_plunder):
    total_plunder = 0
    for i in range(1, days + 1):
        if i % 3 == 0:
            total_plunder += each_plunder * 1.5
        else:
            total_plunder += each_plunder

        if i % 5 == 0:
            total_plunder *= 0.7
    return total_plunder


pirating_days = int(input())
daily_plunder = int(input())
expected_end_plunder = float(input())

collection = plunder(pirating_days, daily_plunder)
if collection >= expected_end_plunder:
    print(f"Ahoy! {collection:.2f} plunder gained.")
else:
    plunder_left_percentage = collection / expected_end_plunder * 100
    print(f"Collected only {plunder_left_percentage:.2f}% of the plunder.")
