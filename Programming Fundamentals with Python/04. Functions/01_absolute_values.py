numbers = list(map(float, input().split(" ")))


def absolute_values(x):
    for i in range(len(x)):
        x[i] = abs(x[i])
    return x


print(absolute_values(numbers))
