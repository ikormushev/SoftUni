first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students = int(input())

maximum_students_per_hour = first_employee + second_employee + third_employee

students_left = students
total_hours = 0
while students_left > 0:
    students_left -= maximum_students_per_hour
    total_hours += 1
    if total_hours % 4 == 0:
        total_hours += 1

print(f"Time needed: {total_hours}h.")
