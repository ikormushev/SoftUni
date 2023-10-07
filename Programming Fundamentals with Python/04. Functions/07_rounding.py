numbers = input().split(" ")


def rounding(x):
    for i in range(len(x)):
        x[i] = round(float(x[i]))
    return x


print(rounding(numbers))
