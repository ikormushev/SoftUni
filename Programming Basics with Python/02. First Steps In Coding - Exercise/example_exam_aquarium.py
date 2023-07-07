length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input()) / 100

volume = length_cm * width_cm * height_cm
volume_lt = volume * 0.001

water_lt = volume_lt - (volume_lt * percent)

print(water_lt)