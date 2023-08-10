K = int(input())
L = int(input())
M = int(input())
N = int(input())

combinations_num = 0
is_valid = False

for n11 in range(K, 9):
    if is_valid:
        break
    if n11 % 2 == 0:
        for n12 in range(9, L - 1, -1):
            if is_valid:
                break
            if n12 % 2 == 1:
                for n21 in range(M, 9):
                    if is_valid:
                        break
                    if n21 % 2 == 0:
                        for n22 in range(9, N - 1, -1):
                            if n22 % 2 == 1:
                                if f"{n11}{n12}" == f"{n21}{n22}":
                                    print("Cannot change the same player.")
                                else:
                                    combinations_num += 1
                                    print(f"{n11}{n12} - {n21}{n22}")
                                    if combinations_num == 6:
                                        is_valid = True
                                        break

