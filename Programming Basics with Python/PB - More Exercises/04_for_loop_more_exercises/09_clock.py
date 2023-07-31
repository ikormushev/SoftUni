minutes = 0
hours = 0

for _ in range(0, 24):
    for _ in range(0, 61):
        if minutes == 60:
            hours += 1
            minutes = 0
            continue
        print(f"{hours} : {minutes:.0f}")
        minutes += 1
