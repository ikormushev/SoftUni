employees_happiness = list(map(int, input().split(" ")))
happiness_factor = int(input())

employees_improved_happiness = [x * happiness_factor for x in employees_happiness]
filtrated_happiness = sum(employees_improved_happiness) / len(employees_improved_happiness)

happier_than_average_employees = [y for y in employees_improved_happiness if y >= filtrated_happiness]

if len(happier_than_average_employees) >= (len(employees_happiness) / 2):
    print(f"Score: {len(happier_than_average_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happier_than_average_employees)}/{len(employees_happiness)}. Employees are not happy!")
