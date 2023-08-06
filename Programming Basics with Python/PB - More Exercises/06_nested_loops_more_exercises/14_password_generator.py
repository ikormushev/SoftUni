first_n = int(input())
second_n = int(input())

for s1 in range(1, first_n + 1):
    for s2 in range(1, first_n + 1):
        for s3 in range(ord("a"), ord("a") + second_n):
            for s4 in range(ord("a"), ord("a") + second_n):
                for s5 in range(1, first_n + 1):
                    if s5 > s1 and s5 > s2:
                        print(f"{s1}{s2}{chr(s3)}{chr(s4)}{s5}", end=" ")
