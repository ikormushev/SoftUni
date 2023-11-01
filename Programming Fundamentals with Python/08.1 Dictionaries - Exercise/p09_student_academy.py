rows_count = int(input())

students = {}

for _ in range(rows_count):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = [student_grade]
    else:
        students[student_name].append(student_grade)

[print(f"{student} -> {(sum(grades) / len(grades)):.2f}")
 for (student, grades) in students.items() if (sum(grades) / len(grades)) >= 4.50]
