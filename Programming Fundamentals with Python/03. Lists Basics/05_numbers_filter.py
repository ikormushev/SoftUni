number = int(input())

numbers = {
    "even": [],
    "odd": [],
    "negative": [],
    "positive": []
}

for _ in range(number + 1):
    command = input()
    if command in ["even", "odd", "negative", "positive"]:
        print(numbers[command])
        break

    new_number = int(command)
    if new_number >= 0:
        numbers["positive"].append(new_number)
    else:
        numbers["negative"].append(new_number)

    if new_number % 2 == 0:
        numbers["even"].append(new_number)
    else:
        numbers["odd"].append(new_number)
