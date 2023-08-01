students_num = int(input())

g1, g2, g3, g4 = 0, 0, 0, 0  # the students in each grade stage
total_grades = 0

for _ in range(1, students_num + 1):
    student_grade = float(input())
    if 2.00 <= student_grade <= 2.99:
        g1 += 1
    elif 3.00 <= student_grade <= 3.99:
        g2 += 1
    elif 4.00 <= student_grade <= 4.99:
        g3 += 1
    elif student_grade >= 5.00:
        g4 += 1
    total_grades += student_grade

average_grade = total_grades / students_num

g1_percent = g1 / students_num * 100
g2_percent = g2 / students_num * 100
g3_percent = g3 / students_num * 100
g4_percent = g4 / students_num * 100

print(f"Top students: {g4_percent:.2f}%")
print(f"Between 4.00 and 4.99: {g3_percent:.2f}%")
print(f"Between 3.00 and 3.99: {g2_percent:.2f}%")
print(f"Fail: {g1_percent:.2f}%")
print(f"Average: {average_grade:.2f}")
