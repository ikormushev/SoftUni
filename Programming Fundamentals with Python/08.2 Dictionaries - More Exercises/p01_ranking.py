contests = {}

contenders = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest_info = command.split(":")
    contest = contest_info[0]
    contest_password = contest_info[1]
    contests[contest] = contest_password

while True:
    command = input()
    if command == "end of submissions":
        break
    user_info = command.split("=>")
    contest = user_info[0]
    contest_password = user_info[1]
    username = user_info[2]
    user_points = int(user_info[3])

    if contest in contests:
        if contests[contest] == contest_password:
            if username not in contenders:
                contenders[username] = {}
                contenders[username][contest] = user_points
            else:
                if contest not in contenders[username]:
                    contenders[username][contest] = user_points
                else:
                    if user_points > contenders[username][contest]:
                        contenders[username][contest] = user_points

total_points = {}
for (name, exams) in contenders.items():
    for (exam, points) in exams.items():
        if name not in total_points:
            total_points[name] = points
        else:
            total_points[name] += points

sorted_total_points = dict(sorted(total_points.items(), key=lambda d: d[1], reverse=True))
contender_with_max_total_points = list(sorted_total_points.keys())[0]
max_total_points = list(sorted_total_points.values())[0]
print(f"Best candidate is {contender_with_max_total_points} "
      f"with total {max_total_points} points.")

sorted_contenders = dict(sorted(contenders.items()))
print("Ranking:")
for name in sorted_contenders.keys():
    print(f"{name}")
    exams = dict(sorted(sorted_contenders[name].items(), key=lambda d: d[1], reverse=True))
    for (exam, points) in exams.items():
        print(f"#  {exam} -> {points}")
