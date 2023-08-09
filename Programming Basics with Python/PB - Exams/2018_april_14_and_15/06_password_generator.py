a = int(input())
b = input().upper()  # capital letter
c = input().lower()  # small letter
d = int(input())
e = int(input())
f = int(input())
n = int(input())

position = 0
password = ""
flag = False

for e1 in range(1, a + 1):
    if flag:
        break
    for e2 in range(ord("A"), ord(b) + 1):
        if flag:
            break
        for e3 in range(ord("a"), ord(c) + 1):
            if flag:
                break
            for e4 in range(1, d + 1):
                if flag:
                    break
                for e5 in range(1, e + 1):
                    if flag:
                        break
                    for e6 in range(1, f + 1):
                        position += 1
                        password = f"{e1}{chr(e2)}{chr(e3)}{e4}{e5}{e6}"
                        if position == n:
                            flag = True
                            break

if flag:
    print(password)
else:
    print("No password on this position")
