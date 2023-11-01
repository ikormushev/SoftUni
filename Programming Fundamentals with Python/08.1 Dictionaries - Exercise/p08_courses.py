students_courses = {}

while True:
    command = input()
    if command == "end":
        break
    course_info = command.split(" : ")
    course_name = course_info[0]
    student_name = course_info[1]

    if course_name not in students_courses:
        students_courses[course_name] = [student_name]
    else:
        students_courses[course_name].append(student_name)

for course, total_students in students_courses.items():
    print(f"{course}: {len(total_students)}")
    for student in total_students:
        print(f"-- {student}")
