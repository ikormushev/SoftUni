first_number_max = int(input())
second_number_max = int(input())
third_number_max = int(input())

for x1 in range(1, first_number_max + 1):
    if x1 % 2 == 0:
        for x2 in range(1, second_number_max + 1):
            count = 0
            for i in range(1, x2 + 1):
                if x2 % i == 0:
                    count += 1
            if count == 2:
                for x3 in range(1, third_number_max + 1):
                    if x3 % 2 == 0:
                        print(f"{x1} {x2} {x3}")
