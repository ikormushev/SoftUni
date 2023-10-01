numbers = input().split(" ")
number = int(input())

numbers_integers = []
people_killed = []
index = 0

for i in range(len(numbers)):
    numbers_integers.append(int(numbers[i]))

people_left = numbers_integers

while len(people_left) > 0:
    index += number - 1
    if index > len(people_left) - 1:
        while index > len(people_left) - 1:
            index -= len(people_left)

    people_killed.append(people_left[index])
    people_left.pop(index)

print("[", end="")
for y in range(len(people_killed)):
    if y < len(people_killed) - 1:
        print(people_killed[y], end=",")
    else:
        print(people_killed[y], end="")
print("]")
