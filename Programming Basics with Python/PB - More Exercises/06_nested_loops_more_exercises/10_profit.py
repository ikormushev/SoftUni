one_lv_num = int(input())
two_lv_num = int(input())
five_lv_num = int(input())
amount = int(input())

for one_lv in range(one_lv_num + 1):
    for two_lv in range(two_lv_num + 1):
        for five_lv in range(five_lv_num + 1):
            if (one_lv * 1 + two_lv * 2 + five_lv * 5) == amount:
                print(f"{one_lv} * 1 lv. + {two_lv} * 2 lv. + "
                      f"{five_lv} * 5 lv. = {amount} lv.")