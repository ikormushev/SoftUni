aquarium_length_cm = int(input())
aquarium_width_cm = int(input())
aquarium_height_cm = int(input())
percent_other_things = float(input()) / 100

water_lt_to_cubic_dm = 1
water_lt_to_cubic_cm = 1000

aquarium_volume_cm = aquarium_length_cm * aquarium_width_cm * aquarium_height_cm
aquarium_volume_dm = aquarium_volume_cm / water_lt_to_cubic_cm

aquarium_volume = aquarium_volume_dm - aquarium_volume_dm * percent_other_things

print(f"{aquarium_volume:.03f}")
