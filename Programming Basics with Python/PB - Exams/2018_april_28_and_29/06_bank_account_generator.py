a = int(input())
b = input()
c = input()
d = input()
e = int(input())
n = int(input())

generated_code = ""
codes_generated = 0
is_max = False

for n1 in range(a, 100):
    if is_max:
        break
    if n1 % 10 == 2:
        for n2 in range(ord(b), ord("Z") + 1):
            if is_max:
                break
            for n3 in range(ord(c), ord("z") + 1):
                if is_max:
                    break
                for n4 in range(ord(d), ord("Z") + 1):
                    if is_max:
                        break
                    for n5 in range(e, 11, -1):
                        if n5 % 10 == 5:
                            generated_code = f"{n1}{chr(n2)}{chr(n3)}{chr(n4)}{n5}"
                            codes_generated += 1
                            if codes_generated >= n:
                                is_max = True
                                break

print(f"{generated_code}")
