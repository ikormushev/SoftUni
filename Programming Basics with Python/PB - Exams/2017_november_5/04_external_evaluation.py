students_num = int(input())

# Poor mark, Satisfactory mark, Good mark, Very good mark, Excellent mark
g1, g2, g3, g4, g5 = 0, 0, 0, 0, 0

for n in range(1, students_num + 1):
    points = float(input())
    if 0 <= points < 22.5:
        g1 += 1
    elif 22.5 <= points < 40.5:
        g2 += 1
    elif 40.5 <= points < 58.5:
        g3 += 1
    elif 58.5 <= points < 76.5:
        g4 += 1
    elif 76.5 <= points <= 100:
        g5 += 1

g1_percent = g1 / students_num * 100
g2_percent = g2 / students_num * 100
g3_percent = g3 / students_num * 100
g4_percent = g4 / students_num * 100
g5_percent = g5 / students_num * 100

print(f"{g1_percent:.2f}% poor marks")
print(f"{g2_percent:.2f}% satisfactory marks")
print(f"{g3_percent:.2f}% good marks")
print(f"{g4_percent:.2f}% very good marks")
print(f"{g5_percent:.2f}% excellent marks")
