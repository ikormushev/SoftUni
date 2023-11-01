companies = {}

while True:
    command = input()
    if command == "End":
        break
    company_info = command.split(" -> ")
    company_name = company_info[0]
    employee_id = company_info[1]

    if company_name not in companies:
        companies[company_name] = [employee_id]
    else:
        if employee_id not in companies[company_name]:
            companies[company_name].append(employee_id)

for company, employees in companies.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")
