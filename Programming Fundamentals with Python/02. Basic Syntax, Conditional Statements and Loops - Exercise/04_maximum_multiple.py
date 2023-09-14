divisor = int(input())
boundary = int(input())

number = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i > 0:
            number = i

print(number)
