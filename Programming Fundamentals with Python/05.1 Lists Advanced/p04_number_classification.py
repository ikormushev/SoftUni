def printing_numbers(numbers: list):
    for i in range(len(numbers)):
        if i % 2 == 0:
            print(numbers[i], end="")
            continue
        else:
            if len(numbers[i]) == 0:
                print()
            else:
                for y in range(len(numbers[i])):
                    if y == len(numbers[i]) - 1:
                        print(f" {numbers[i][y]}")
                        break
                    print(f" {numbers[i][y]}", end=",")


starting_numbers = list(map(int, input().split(", ")))

new_numbers = ["Positive:", [p for p in starting_numbers if p >= 0],
               "Negative:", [n for n in starting_numbers if n < 0],
               "Even:", [e for e in starting_numbers if e % 2 == 0],
               "Odd:", [o for o in starting_numbers if o % 2 == 1]]

printing_numbers(new_numbers)
