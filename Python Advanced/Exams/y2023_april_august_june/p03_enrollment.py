def gather_credits(credits_needed, *args):
    current_credits = 0
    courses = []

    for i in range(len(args)):
        if current_credits >= credits_needed:  # not all tests pass if this statement is not at the start of the loop
            break
        course_name, course_credits = args[i]
        if course_name in courses:
            continue

        courses.append(course_name)
        current_credits += course_credits

    string_to_print = ""

    if current_credits < credits_needed:
        credits_diff = credits_needed - current_credits
        string_to_print += (f"You need to enroll in more courses! "
                            f"You have to gather {credits_diff} credits more.")
    else:
        sorted_courses = sorted(courses)
        string_to_print += f"Enrollment finished! Maximum credits: {current_credits}.\n"
        string_to_print += f"Courses: {', '.join(sorted_courses)}"

    return string_to_print


print(gather_credits(80, ("Basics", 27), ))

print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27), ))

print(gather_credits(60, ("Basics", 27), ("Fundamentals", 27), ("Advanced", 30), ("Web", 30)))
