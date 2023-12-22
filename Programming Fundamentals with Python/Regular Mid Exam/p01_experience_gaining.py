total_experience = float(input())
total_battles = int(input())

collected_experience = 0
battles_count = 0

for i in range(1, total_battles + 1):
    experience_gained = float(input())
    if i % 15 == 0:
        experience_gained *= 1.05
    elif i % 3 == 0:
        experience_gained *= 1.15
    elif i % 5 == 0:
        experience_gained *= 0.90
    battles_count += 1
    collected_experience += experience_gained
    if collected_experience >= total_experience:
        break

if collected_experience >= total_experience:
    print(f"Player successfully collected his needed experience for {battles_count} battles.")
else:
    experience_diff = total_experience - collected_experience
    print(f"Player was not able to collect the needed experience, {experience_diff:.2f} more needed.")
