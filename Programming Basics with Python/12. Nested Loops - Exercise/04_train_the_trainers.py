jury_num = int(input())

average_grade_total = 0
presentations_num = 0

while True:
    command = input()
    if command == "Finish":
        average_grade_total *= 1 / (presentations_num * jury_num)
        print(f"Student's final assessment is {average_grade_total:.2f}.")
        break
    presentation_name = command
    presentations_num += 1
    grades_total = 0
    average_grade = 0
    for _ in range(1, jury_num + 1):
        grade = float(input())
        grades_total += grade
        average_grade_total += grade
    average_grade = grades_total / jury_num
    print(f"{presentation_name} - {average_grade:.2f}.")
