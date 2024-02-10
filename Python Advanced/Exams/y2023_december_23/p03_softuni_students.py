def softuni_students(*args, **kwargs):
    students = {}

    for (student_id, name) in args:
        students[name] = {}
        students[name]["student_id"] = student_id
        students[name]["course"] = ""

    for (student_id, course) in kwargs.items():
        for (student_name, student_info) in students.items():
            if student_info["student_id"] == student_id:
                students[student_name]["course"] = course

    sorted_students = dict(sorted(students.items(), key=lambda d: d[0]))

    string_to_print = ""
    invalid_course_students = []

    for (student_name, student_info) in sorted_students.items():
        if student_info["course"]:
            string_to_print += (f"*** A student with the username {student_name} "
                                f"has successfully finished the course {student_info['course']}!\n")
        else:
            invalid_course_students.append(student_name)

    if invalid_course_students:
        string_to_print += f"!!! Invalid course students: {', '.join(invalid_course_students)}"

    return string_to_print


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))