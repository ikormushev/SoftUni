from math import log

number = int(input())
logarithm_base = input()
logarithm = 0

if logarithm_base == "natural":
    logarithm = log(number)
else:
    logarithm = log(number, int(logarithm_base))

print(f"{logarithm:.2f}")
