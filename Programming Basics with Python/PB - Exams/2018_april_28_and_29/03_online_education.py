type_of_education_first_stage = input()
first_stage_students = int(input())
type_of_education_second_stage = input()
second_stage_students = int(input())
type_of_education_third_stage = input()
third_stage_students = int(input())

onsite_students = 0
online_students = 0

if type_of_education_first_stage == "onsite":
    onsite_students += first_stage_students
elif type_of_education_first_stage == "online":
    online_students += first_stage_students

if type_of_education_second_stage == "onsite":
    onsite_students += second_stage_students
elif type_of_education_second_stage == "online":
    online_students += second_stage_students

if type_of_education_third_stage == "onsite":
    onsite_students += third_stage_students
elif type_of_education_third_stage == "online":
    online_students += third_stage_students

onsite_diff = 600 - onsite_students
if onsite_diff < 0:
    onsite_students += onsite_diff
    online_students -= onsite_diff

total_students = onsite_students + online_students

print(f"Online students: {online_students}")
print(f"Onsite students: {onsite_students}")
print(f"Total students: {total_students}")
