first_num = input()
second_num = input()

new_first_number = 0
even_sum = 0
odd_sum = 0
equal_nums = ""

if first_num < second_num:
    for i in range(int(first_num), int(second_num) + 1):
        new_first_number = str(i)
        even_sum = 0
        odd_sum = 0
        for n in range(0, len(new_first_number)):
            if n % 2 == 0:
                even_sum += int(new_first_number[n])
            else:
                odd_sum += int(new_first_number[n])
        if even_sum == odd_sum:
            equal_nums += f"{new_first_number} "
    print(f"{equal_nums}")
else:
    pass
