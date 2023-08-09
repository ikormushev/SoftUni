interval_start = int(input())
interval_end = int(input())

# even = False
# odd = False

for n1 in range(interval_start, interval_end + 1):
    even = False
    odd = False
    if n1 % 2 == 0:
        even = True
    else:
        odd = True
    for n2 in range(interval_start, interval_end + 1):
        for n3 in range(interval_start, interval_end + 1):
            if (n2 + n3) % 2 == 0:
                for n4 in range(interval_start, interval_end + 1):
                    if n4 < n1:
                        if even and (n4 % 2 == 1):
                            print(f"{n1}{n2}{n3}{n4}", end=" ")
                        elif odd and (n4 % 2 == 0):
                            print(f"{n1}{n2}{n3}{n4}", end=" ")
