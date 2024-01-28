numbers = [int(x) for x in input().split()]
n = int(input())

for _ in range(n):
    index = int(input())

    try:
        print(numbers[index])
        print(1/index)
    except (IndexError, ZeroDivisionError):
        print("Invalid input")
    finally:
        print("Just doing finally stuff")

print("End")
