number = int(input())

count = 0
is_prime = False

for i in range(1, number + 1):
    if number % i == 0:
        count += 1

if count == 2:
    is_prime = True

print(is_prime)