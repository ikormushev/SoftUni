courses_num = int(input())

credit_system = {
    2: 0,
    3: 0.50,
    4: 0.70,
    5: 0.85,
    6: 1
}

grades = 0
total_credits = 0

for _ in range(1, courses_num + 1):
    number = int(input())
    grade = number % 10
    credit = number // 10

    courses_credits = credit * credit_system[grade]
    total_credits += courses_credits
    grades += grade

average_grade = grades / courses_num

print(f"{total_credits:.2f}")
print(f"{average_grade:.2f}")
