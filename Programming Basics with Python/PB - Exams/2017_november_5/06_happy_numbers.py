number = int(input())

for n1 in range(1, 10):
    for n2 in range(1, 10):
        for n3 in range(1, 10):
            for n4 in range(1, 10):
                if (n1 + n2) == (n3 + n4):
                    happy_number = f"{n1}{n2}{n3}{n4}"
                    if number % (n1 + n2) == 0:
                        print(happy_number, end=" ")
