students = {}
courses = []

while True:
    command = input()
    if command in courses:
        for (name, name_id) in students.items():
            if name_id[1] == command:
                print(f"{name} - {name_id[0]}")
        break
    student_info = command.split(":")
    student_name = student_info[0]
    student_id = student_info[1]
    course = list(student_info[2])

    if " " in course:
        for i in range(len(course)):
            if course[i] == " ":
                course[i] = "_"
    new_course = "".join(course)
    if new_course not in courses:
        courses.append(new_course)

    students[student_name] = [student_id, new_course]  # inserts both values as a list

