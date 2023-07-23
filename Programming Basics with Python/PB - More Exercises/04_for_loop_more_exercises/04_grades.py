students_num = int(input())

g1, g2, g3, g4 = 0, 0, 0, 0
total_grade = 0

for i in range(students_num):
    grade = float(input())
    total_grade += grade
    if 2.00 <= grade <= 2.99:
        g1 += 1
    elif 3.00 <= grade <= 3.99:
        g2 += 1
    elif 4.00 <= grade <= 4.99:
        g3 += 1
    elif grade >= 5.00:
        g4 += 1

average_grade = total_grade / students_num
g1_percent = g1 / students_num * 100
g2_percent = g2 / students_num * 100
g3_percent = g3 / students_num * 100
g4_percent = g4 / students_num * 100

print(f"Top students: {g4_percent:.2f}%")
print(f"Between 4.00 and 4.99: {g3_percent:.2f}%")
print(f"Between 3.00 and 3.99: {g2_percent:.2f}%")
print(f"Fail: {g1_percent:.2f}%")
print(f"Average: {average_grade:.2f}")
