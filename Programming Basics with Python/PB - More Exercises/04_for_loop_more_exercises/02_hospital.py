period = int(input())

doctors_num = 7
patients_coming = 0
patients_left = 0
patients_helped = 0

for i in range(1, period + 1):
    if i % 3 == 0 and patients_helped < patients_left:
        doctors_num += 1
    patients_coming = int(input())
    if patients_coming <= doctors_num:
        patients_helped_per_day = patients_coming
    else:
        patients_helped_per_day = doctors_num
    patients_left_per_day = patients_coming - patients_helped_per_day
    patients_helped += patients_helped_per_day
    patients_left += patients_left_per_day


print(f"Treated patients: {patients_helped}.")
print(f"Untreated patients: {patients_left}.")
