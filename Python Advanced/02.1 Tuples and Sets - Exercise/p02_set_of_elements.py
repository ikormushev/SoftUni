numbers = input().split()
n = int(numbers[0])
m = int(numbers[1])

first_set = set([input() for _ in range(n)])
second_set = set([input() for _ in range(m)])

[print(x) for x in first_set & second_set]
