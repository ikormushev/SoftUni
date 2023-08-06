a = int(input())
b = int(input())
passwords_max_num = int(input())

passwords_num = 0
max_reached = False
l1 = ord(chr(35))
l2 = ord(chr(64))

for l3 in range(1, a + 1):
    if max_reached:
        break
    for l4 in range(1, b + 1):
        if passwords_num >= passwords_max_num:
            max_reached = True
            break
        if l1 > 55:
            l1 = 35
        if l2 > 96:
            l2 = 64
        passwords_num += 1
        print(f"{chr(l1)}{chr(l2)}{l3}{l4}{chr(l2)}{chr(l1)}", end="|")
        l1 += 1
        l2 += 1
