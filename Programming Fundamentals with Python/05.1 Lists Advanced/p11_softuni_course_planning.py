initial_schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    modifying_command = command.split(":")
    lesson = modifying_command[1]
    exercise = lesson + "-" + "Exercise"

    if "Add" in modifying_command:
        if lesson not in initial_schedule:
            initial_schedule.append(lesson)

    elif "Insert" in modifying_command:
        index = int(modifying_command[2])
        if lesson not in initial_schedule:
            initial_schedule.insert(index, lesson)

    elif "Remove" in modifying_command:
        if lesson in initial_schedule:
            initial_schedule.remove(lesson)
            if exercise in initial_schedule:
                initial_schedule.remove(exercise)

    elif "Swap" in modifying_command:
        lesson_index = initial_schedule.index(lesson)
        other_lesson = modifying_command[2]
        other_lesson_exercise = other_lesson + "-" + "Exercise"
        if lesson in initial_schedule and other_lesson in initial_schedule:
            other_lesson_index = initial_schedule.index(other_lesson)
            (initial_schedule[lesson_index],initial_schedule[other_lesson_index]) = \
                (initial_schedule[other_lesson_index], initial_schedule[lesson_index])
            other_lesson_index = initial_schedule.index(other_lesson)

            if exercise in initial_schedule:
                initial_schedule.remove(exercise)
                initial_schedule.insert(lesson_index + 1, exercise)

            if other_lesson_exercise in initial_schedule:
                initial_schedule.remove(other_lesson_exercise)
                initial_schedule.insert(other_lesson_index + 1, other_lesson_exercise)

    elif "Exercise" in modifying_command:
        if lesson in initial_schedule and exercise not in initial_schedule:
            lesson_index = initial_schedule.index(lesson)
            exercise_index = lesson_index + 1
            initial_schedule.insert(exercise_index, exercise)
        elif lesson not in initial_schedule:
            initial_schedule.append(lesson)
            initial_schedule.append(exercise)

for i in range(1, len(initial_schedule) + 1):
    print(f"{i}.{initial_schedule[i - 1]}")
