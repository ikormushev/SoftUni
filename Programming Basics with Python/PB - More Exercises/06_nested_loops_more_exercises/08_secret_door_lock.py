hundreds_max = int(input())
tens_max = int(input())
ones_max = int(input())

for n1 in range(1, hundreds_max + 1):
    if n1 % 2 == 0:
        for n2 in range(1, tens_max + 1):
            count = 0
            for i in range(1, n2 + 1):
                if n2 % i == 0:
                    count += 1
            if count == 2:
                for n3 in range(1, ones_max + 1):
                    if n3 % 2 == 0:
                        print(f"{n1} {n2} {n3}")
