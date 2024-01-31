from collections import deque

food_portions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])
mountain_peaks = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])
conquered_peaks = deque()

while food_portions and stamina and mountain_peaks:
    food = food_portions.pop()
    daily_stamina = stamina.popleft()
    peak_name, peak_level = mountain_peaks.popleft()
    if food + daily_stamina >= peak_level:
        conquered_peaks.append(peak_name)
    else:
        mountain_peaks.appendleft((peak_name, peak_level))

if not mountain_peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    while conquered_peaks:
        print(conquered_peaks.popleft())
