def students_credits(*args):
    courses = {}
    all_credits = 0
    for i in range(len(args)):
        info = args[i].split("-")
        course_name = info[0]
        course_credits = int(info[1])
        max_test_points = int(info[2])
        diyan_points = int(info[3])

        proportion = diyan_points / max_test_points
        diyan_credits = course_credits * proportion
        all_credits += diyan_credits

        courses[course_name] = diyan_credits

    sorted_courses = dict(sorted(courses.items(), key= lambda d: -d[1]))

    string_to_print = ""
    if all_credits >= 240:
        string_to_print += f"Diyan gets a diploma with {all_credits:.1f} credits.\n"
    else:
        string_to_print += f"Diyan needs {240 - all_credits:.1f} credits more for a diploma.\n"

    for (course, d_credits) in sorted_courses.items():
        string_to_print += f"{course} - {d_credits:.1f}\n"

    return string_to_print


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)