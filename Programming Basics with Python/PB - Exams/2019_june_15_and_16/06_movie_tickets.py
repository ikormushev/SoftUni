a1 = int(input())
a2 = int(input())
n = int(input())

for s1 in range(a1, a2):
    if s1 % 2 == 1:
        for s2 in range(1, n):
            for s3 in range(1, int(n / 2)):
                if (s2 + s3 + s1) % 2 == 1:
                    print(f"{chr(s1)}-{s2}{s3}{s1}")
