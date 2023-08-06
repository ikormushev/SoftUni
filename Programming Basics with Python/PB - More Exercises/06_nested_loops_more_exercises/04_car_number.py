interval_start = int(input())
interval_end = int(input())

for n1 in range(interval_start, interval_end + 1):
    for n2 in range(interval_start, interval_end + 1):
        for n3 in range(interval_start, interval_end + 1):
            for n4 in range(interval_start, interval_end + 1):
                if n1 % 2 == 0 and n4 % 2 == 0:
                    continue
                elif n1 % 2 == 1 and n4 % 2 == 1:
                    continue
                if n4 > n1:
                    continue
                if (n2 + n3) % 2 == 1:
                    continue
                print(f"{n1}{n2}{n3}{n4}", end=" ")
