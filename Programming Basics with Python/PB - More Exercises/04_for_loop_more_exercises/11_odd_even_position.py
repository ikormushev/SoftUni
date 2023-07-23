from sys import maxsize

number = int(input())

odd_sum = 0
odd_min = maxsize
odd_max = -maxsize
even_sum = 0
even_min = maxsize
even_max = -maxsize

for i in range(1, number + 1):
    new_number = float(input())
    if i % 2 == 1:
        odd_sum += new_number
        if new_number > odd_max:
            odd_max = new_number
        if new_number < odd_min:
            odd_min = new_number
    else:
        even_sum += new_number
        if new_number > even_max:
            even_max = new_number
        if new_number < even_min:
            even_min = new_number

print(f"OddSum={odd_sum:.2f},")
if odd_min == maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_min == maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
