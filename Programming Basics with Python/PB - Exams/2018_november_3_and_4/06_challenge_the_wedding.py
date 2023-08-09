men = int(input())
women = int(input())
tables_max = int(input())

tables_num = 0
flag = False

for p1 in range(1, men + 1):
    if flag:
        break
    for p2 in range(1, women + 1):
        print(f"({p1} <-> {p2})", end=" ")
        tables_num += 1
        if tables_num >= tables_max:
            flag = True
            break
