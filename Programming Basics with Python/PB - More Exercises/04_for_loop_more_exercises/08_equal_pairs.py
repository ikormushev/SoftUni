n = int(input())

first_pair = 0
first_diff = 0

for i in range(1, n + 1):
    first_number = int(input())
    second_number = int(input())
    pair = first_number + second_number
    if i == 1:
        first_pair = pair
        continue
    diff = abs(pair - first_pair)
    if diff > first_diff:
        first_diff = diff
    first_pair = pair

if first_diff == 0:
    print(f"Yes, value={first_pair}")
else:
    print(f"No, maxdiff={first_diff}")
