from math import ceil

people_num = int(input())
elevator_capacity = int(input())

elevator_courses = ceil(people_num / elevator_capacity)

print(elevator_courses)
