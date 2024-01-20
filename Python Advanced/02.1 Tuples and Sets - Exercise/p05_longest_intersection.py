number = int(input())

largest_intersection = []

for _ in range(number):
    info = input().split("-")
    first = info[0].split(",")
    second = info[1].split(",")
    first_start = int(first[0])
    first_end = int(first[1])
    second_start = int(second[0])
    second_end = int(second[1])

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))
    final_set = first_set & second_set
    if len(final_set) > len(largest_intersection):
        largest_intersection = list(final_set)

print(f"Longest intersection is {largest_intersection} with length {len(largest_intersection)}")
