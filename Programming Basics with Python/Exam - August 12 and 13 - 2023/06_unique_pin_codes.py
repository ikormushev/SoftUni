number_one_upper_limit = int(input())
number_two_upper_limit = int(input())
number_three_upper_limit = int(input())


for n1 in range(1, number_one_upper_limit + 1):
    if n1 % 2 == 0:
        for n2 in range(1, number_two_upper_limit + 1):
            count = 0
            for i in range(1, n2 + 1):
                if n2 % i == 0:
                    count += 1
            if count == 2 and n2 != 1:
                for n3 in range(1, number_three_upper_limit + 1):
                    if n3 % 2 == 0:
                        print(f"{n1} {n2} {n3}")
