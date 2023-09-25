number = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(number):
    new_number = int(input())
    if new_number >= 0:
        positive_numbers.append(new_number)
    else:
        negative_numbers.append(new_number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
