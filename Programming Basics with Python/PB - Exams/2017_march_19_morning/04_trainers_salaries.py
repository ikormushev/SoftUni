from decimal import Decimal, ROUND_HALF_UP  # importing the library because formatting isn't working as intended

trainers_num = int(input())
budget = float(input())

budget = Decimal(str(budget))
money_per_lecture = budget / trainers_num

trainers_salary = {
    "Jelev": Decimal("0"),
    "RoYaL": Decimal("0"),
    "Roli": Decimal("0"),
    "Trofon": Decimal("0"),
    "Sino": Decimal("0")
}

others_salary = Decimal("0")

for i in range(trainers_num):
    trainer_name = input()
    if trainer_name in trainers_salary:
        trainers_salary[trainer_name] += money_per_lecture
    else:
        others_salary += money_per_lecture

salary_jelev = Decimal(str(trainers_salary["Jelev"])).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
salary_royal = Decimal(str(trainers_salary["RoYaL"])).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
salary_roli = Decimal(str(trainers_salary["Roli"])).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
salary_trofon = Decimal(str(trainers_salary["Trofon"])).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
salary_sino = Decimal(str(trainers_salary["Sino"])).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
salary_others = Decimal(str(others_salary)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f'Jelev salary: {salary_jelev} lv')
print(f'RoYaL salary: {salary_royal} lv')
print(f'Roli salary: {salary_roli} lv')
print(f'Trofon salary: {salary_trofon} lv')
print(f'Sino salary: {salary_sino} lv')
print(f'Others salary: {salary_others} lv')

# If we don't import the library, there may be issues with formatting the outputs with '{0:.2f}'.format() .
# For example - with an input (4, 750.50, other, other, other, Roli):
# Roli's salary is 187.625. The program formats it to 187.62, which shouldn't be the case - it should be 187.63.
# Meanwhile, Others' salary is 562.875 and the program formats it the right way - to 562.88.
