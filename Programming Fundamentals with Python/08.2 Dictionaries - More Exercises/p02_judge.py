contests = {}
users_individual_standings = {}

while True:
    command = input()
    if command == "no more time":
        break
    judge_command = command.split(" -> ")
    username, contest, points = judge_command[0], judge_command[1], int(judge_command[2])

    if username not in users_individual_standings:
        users_individual_standings[username] = 0

    if contest not in contests:
        contests[contest] = {username: points}
        users_individual_standings[username] += points
    else:
        if username not in contests[contest]:
            contests[contest][username] = points
            users_individual_standings[username] += points
        else:
            if points > contests[contest][username]:
                users_individual_standings[username] += points - contests[contest][username]
                contests[contest][username] = points


for (contest_name, users) in contests.items():
    user_num = 1
    print(f"{contest_name}: {len(contests[contest_name].keys())} participants")

    # Now we have to sort the dictionary
    sorted_users_by_points = dict(sorted(contests[contest_name].items(), key=lambda d: (-d[1], d[0])))
    # the lambda function:
    # -d[1] represents the points in descending (because of the minus) order
    # if there is a tie, the second condition is used - d[0], which represents the names

    for (user, user_points) in sorted_users_by_points.items():
        print(f"{user_num}. {user} <::> {user_points}")
        user_num += 1

users_individual_standings = dict(sorted(users_individual_standings.items(), key=lambda d: (-d[1], d[0])))
print("Individual standings:")
user_num = 1
for (user, total_points) in users_individual_standings.items():
    print(f"{user_num}. {user} -> {total_points}")
    user_num += 1
