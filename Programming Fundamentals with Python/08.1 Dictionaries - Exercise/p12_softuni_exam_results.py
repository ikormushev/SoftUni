exam_results = {}
languages_submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break
    exam = command.split("-")
    username = exam[0]
    if "banned" in exam:
        del exam_results[username]
        continue
    exam_language = exam[1]
    exam_points = int(exam[2])

    if username not in exam_results:
        exam_results[username] = {}
        exam_results[username][exam_language] = [exam_points]
    else:
        if exam_language in exam_results[username]:
            exam_results[username][exam_language].append(exam_points)
        else:
            exam_results[username][exam_language] = [exam_points]

    if exam_language not in languages_submissions:
        languages_submissions[exam_language] = 1
    else:
        languages_submissions[exam_language] += 1

print("Results:")
for (name, languages) in exam_results.items():
    for (language, points) in languages.items():
        print(f"{name} | {max(points)}")

print(f"Submissions:")
[print(f"{language} - {submissions}") for (language, submissions) in languages_submissions.items()]
