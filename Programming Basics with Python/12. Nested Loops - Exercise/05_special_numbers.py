number = int(input())

is_division = False

for i in range(1111, 10000):
    special_number = str(i)
    for n in range(len(special_number)):
        if int(special_number[n]) == 0:
            is_division = False
            break
        elif number % int(special_number[n]) == 0:
            is_division = True
        else:
            is_division = False
            break
    if is_division:
        print(i, end=" ")
