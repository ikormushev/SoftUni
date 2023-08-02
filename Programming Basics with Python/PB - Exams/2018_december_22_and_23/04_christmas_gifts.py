kids = 0
adults = 0

while True:
    command = input()
    if command == "Christmas":
        break
    person_age = int(command)
    if person_age <= 16:
        kids += 1
    else:
        adults += 1

toys = kids * 5
sweaters = adults * 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys}")
print(f"Money for sweaters: {sweaters}")
