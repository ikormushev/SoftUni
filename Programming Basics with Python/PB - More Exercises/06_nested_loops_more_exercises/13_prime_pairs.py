start_amount_first_p = int(input())
start_amount_second_p = int(input())
diff_start_end_first_p = int(input())
diff_start_end_second_p = int(input())

end_amount_first_p = start_amount_first_p + diff_start_end_first_p
end_amount_second_p = start_amount_second_p + diff_start_end_second_p

n1_count = 0
n2_count = 0

for n1 in range(start_amount_first_p, end_amount_first_p + 1):
    is_n1_prime = False
    n1_count = 0

    for i in range(1, n1 + 1):
        if n1 % i == 0:
            n1_count += 1
    if n1_count == 2:
        is_n1_prime = True

    for n2 in range(start_amount_second_p, end_amount_second_p + 1):
        is_n2_prime = False
        n2_count = 0

        for y in range(1, n2 + 1):
            if n2 % y == 0:
                n2_count += 1
        if n2_count == 2:
            is_n2_prime = True

        if is_n1_prime and is_n2_prime:
            print(f"{n1}{n2}")
