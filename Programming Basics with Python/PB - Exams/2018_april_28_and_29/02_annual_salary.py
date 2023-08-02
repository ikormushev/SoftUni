experience_years = int(input())
specialization = input()

specializations_salaries = {
    "C# Developer": 5400,
    "Java Developer": 5700,
    "Front-End Web Developer": 4100,
    "UX / UI Designer": 3100,
    "Game Designer": 3600
}

monthly_salary = specializations_salaries[specialization]

if experience_years <= 5:
    monthly_salary *= 0.342

annual_salary = monthly_salary * 12

print(f"Total earned money: {annual_salary:.2f} BGN")
