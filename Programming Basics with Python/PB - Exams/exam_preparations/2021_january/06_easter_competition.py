breads_num = int(input())

winner_points = 0
winner_name = ""

for _ in range(1, breads_num + 1):
    baker_name = input()
    baker_points = 0
    while True:
        command = input()
        if command == "Stop":
            print(f"{baker_name} has {baker_points} points.")
            if baker_name == winner_name:
                print(f"{baker_name} is the new number 1!")
            break
        bread_grade = int(command)
        baker_points += bread_grade

        if baker_points > winner_points:
            winner_points = baker_points
            winner_name = baker_name

print(f"{winner_name} won competition with {winner_points} points!")
