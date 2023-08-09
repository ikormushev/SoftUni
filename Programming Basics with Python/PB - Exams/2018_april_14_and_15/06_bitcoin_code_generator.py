a = int(input())
b = int(input())
max_codes = int(input())

l1 = ord(chr(33))
l2 = ord(chr(58))
flag = False
codes_num = 0

for x in range(1, a + 1):
    if flag:
        break
    for y in range(1, b + 1):
        if l1 > 47:
            l1 = 33
        if l2 > 64:
            l2 = 58

        codes_num += 1
        print(f"{chr(l1)}{chr(l2)}{x}{y}{chr(l2)}{chr(l1)}", end="|")
        l1 += 1
        l2 += 1

        if codes_num >= max_codes:
            flag = True
            break
