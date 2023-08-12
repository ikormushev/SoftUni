wanted_height_cm = int(input())

next_jump = wanted_height_cm - 30
jumps_tried = 0

failed_jumps = 0
failed_training = False

while True:
    jump = int(input())
    jumps_tried += 1
    if jump >= wanted_height_cm:
        break
    if jump > next_jump:
        next_jump += 5
        failed_jumps = 0
    else:
        failed_jumps += 1
        if failed_jumps == 3:
            failed_training = True
            break

if failed_training:
    print(f"Tihomir failed at {next_jump}cm after {jumps_tried} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {next_jump}cm after {jumps_tried} jumps.")
