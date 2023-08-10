number = int(input())

new_number = number
N = int(str(number)[0]) + int(str(number)[1])
M = int(str(number)[0]) + int(str(number)[2])

for x in range(N):
    for y in range(M):
        if new_number % 5 == 0:
            new_number -= int(str(number)[0])
        elif new_number % 3 == 0:
            new_number -= int(str(number)[1])
        else:
            new_number += int(str(number)[2])
        print(f"{new_number}", end=" ")
    print()

