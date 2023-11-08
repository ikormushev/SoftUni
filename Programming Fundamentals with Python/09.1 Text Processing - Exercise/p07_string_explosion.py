total_explosions = input()

explosions = 0
final_string = ""

for i in range(len(total_explosions)):
    if explosions > 0 and total_explosions[i] != ">":
        explosions -= 1
        continue

    if total_explosions[i] == ">":
        bombings = int(total_explosions[i + 1])
        explosions += bombings
    final_string += total_explosions[i]

print(final_string)