clothes_box = [int(cloth) for cloth in input().split()]
rack_capacity = int(input())
total_racks = 0

previous_cloth = 0
clothes_sum = 0

while clothes_box:
    if clothes_sum == 0:
        clothes_sum += previous_cloth

    cloth = clothes_box.pop()
    clothes_sum += cloth

    if clothes_sum >= rack_capacity:
        total_racks += 1
        previous_cloth = 0 if clothes_sum == rack_capacity else cloth
        clothes_sum = 0

if previous_cloth:
    total_racks += 1

print(total_racks)
