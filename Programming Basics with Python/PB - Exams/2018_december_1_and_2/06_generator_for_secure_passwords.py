a = int(input())
b = int(input())
max_passwords_generated = int(input())

passwords_count = 0
flag = False

l1 = ord((chr(35)))
l2 = ord(chr(64))

for l3 in range(1, a + 1):
    if flag:
        break
    for l4 in range(1, b + 1):
        if passwords_count >= max_passwords_generated:
            flag = True
            break
        if l1 > 55:
            l1 = 35
        if l2 > 96:
            l2 = 64
        passwords_count += 1
        print(f"{chr(l1)}{chr(l2)}{l3}{l4}{chr(l2)}{chr(l1)}", end="|")
        l1 += 1
        l2 += 1
