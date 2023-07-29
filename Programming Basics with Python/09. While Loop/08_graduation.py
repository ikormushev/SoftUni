student_name = input()

total_grade = 0
years = 0
incompletions_num = 0

while True:
    annual_grade = float(input())
    if annual_grade >= 4.00:
        total_grade += annual_grade
        years += 1
    elif annual_grade < 4.00:
        incompletions_num += 1
        if incompletions_num > 1:
            years += 1
            print(f"{student_name} has been excluded at {years} grade")
            break
        continue
    if years == 12:
        average_grade = total_grade / 12
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break
