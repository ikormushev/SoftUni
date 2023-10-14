numbers = list(map(int, input().split(", ")))

maximum_tens = (max(numbers) // 10) + 1

for i in range(1, maximum_tens + 1):
    tens_list = [x for x in numbers if (i - 1) * 10 < x <= i * 10]
    if len(tens_list) == 0 and i == maximum_tens:
        break
    print(f"Group of {i}0's: {tens_list}")
