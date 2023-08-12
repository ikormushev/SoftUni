interval_start = int(input())
interval_end = int(input())

for n1 in range(int(str(interval_start)[0]), int(str(interval_end)[0]) + 1):
    if n1 % 2 == 1:
        for n2 in range(int(str(interval_start)[1]), int(str(interval_end)[1]) + 1):
            if n2 % 2 == 1:
                for n3 in range(int(str(interval_start)[2]), int(str(interval_end)[2]) + 1):
                    if n3 % 2 == 1:
                        for n4 in range(int(str(interval_start)[3]), int(str(interval_end)[3]) + 1):
                            if n4 % 2 == 1:
                                print(f"{n1}{n2}{n3}{n4}", end=" ")
