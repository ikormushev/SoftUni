intelligence = int(input())
power = int(input())
gender = input()

role = ""

if intelligence >= 80:
    if power >= 80 and gender == "female":
        role = "Queen Bee"
    else:
        role = "Repairing Bee"
elif intelligence >= 60:
    role = "Cleaning Bee"
else:
    if power >= 80 and gender == "male":
        role = "Drone Bee"
    elif power >= 60:
        role = "Guard Bee"
    else:
        role = "Worker Bee"

print(role)
