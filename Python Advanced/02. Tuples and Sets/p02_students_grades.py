students_num = int(input())
students_info = {}

for _ in range(students_num):
    info = tuple(input().split())
    name = info[0]
    grade = float(info[1])
    if name not in students_info:
        students_info[name] = []
    students_info[name].append(grade)

for (student, grades) in students_info.items():
    print(f"{student} -> ", end="")
    for last_grade in grades:
        print(f"{last_grade:.2f}", end=" ")
    print(f"(avg: {(sum(grades) / len(grades)):.2f})")
