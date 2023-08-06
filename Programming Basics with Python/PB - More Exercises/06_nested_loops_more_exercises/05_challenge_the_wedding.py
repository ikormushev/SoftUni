men_num = int(input())
women_num = int(input())
tables_max = int(input())

tables_used = 0
tables_limit = False

for m in range(1, men_num + 1):
    if tables_limit:
        break
    for w in range(1, women_num + 1):
        if tables_used >= tables_max:
            tables_limit = True
            break
        tables_used += 1
        print(f"({m} <-> {w})", end=" ")
