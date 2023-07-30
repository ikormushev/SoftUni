fail_cap = int(input())

problem_name = ""
problems_num = 0
grades = 0
poor_grades = 0

while True:
    name = input()
    if name == "Enough":
        average_grade = grades / problems_num
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {problems_num}")
        print(f"Last problem: {problem_name}")
        break
    problem_name = name
    problems_num += 1
    grade = int(input())
    if grade <= 4:
        poor_grades += 1
        if poor_grades == fail_cap:
            print(f"You need a break, {poor_grades} poor grades.")
            break
    grades += grade
