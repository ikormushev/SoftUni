numbers = tuple([float(x) for x in input().split()])

number_occurrences = {}

for number in numbers:
    if number not in number_occurrences:
        number_occurrences[number] = numbers.count(number)

for (number, occurrence) in number_occurrences.items():
    print(f"{number} - {occurrence} times")
