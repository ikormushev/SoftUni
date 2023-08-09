capital = input()
first_small = input()
second_small = input()
third_small = input()
number = int(input())

recommendations_num = -1  # we need to find the recommendations_num UNTIL a name is chosen

for l1 in range(ord("A"), ord(capital) + 1):
    for l2 in range(ord("a"), ord(first_small) + 1):
        for l3 in range(ord("a"), ord(second_small) + 1):
            for l4 in range(ord("a"), ord(third_small) + 1):
                for l5 in range(0, number + 1):
                    recommendations_num += 1

print(recommendations_num)
