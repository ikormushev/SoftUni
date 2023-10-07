number = int(input())


def loading_up_to_hundred():
    print(f"{number}% ", end="")
    for i in range(int(number / 10)):
        if i == 0:
            print("[%", end="")
        else:
            print("%", end="")

    for j in range(10 - int(number / 10)):
        if number == 0 and j == 0:
            print("[.", end="")
        elif j == (10 - int(number / 10) - 1):
            print(".]")
        else:
            print(".", end="")
    print("Still loading...")


def loaded():
    print(f"{number}% Complete!")
    print("[%%%%%%%%%%]")


if number < 100:
    loading_up_to_hundred()
else:
    loaded()
