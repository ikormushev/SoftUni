from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars_line = deque()
cars_safely_passed = 0

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{cars_safely_passed} total cars passed the crossroads.")
        break
    elif command == "green":
        green_time_available = green_light_duration
        current_car = []

        while green_time_available > 0:
            if cars_line:
                current_car = cars_line.popleft()
            else:
                break
            green_time_available -= len(current_car)
            if green_time_available >= 0:
                cars_safely_passed += 1
            else:
                if green_time_available + free_window_duration >= 0:
                    cars_safely_passed += 1
                    current_car = []
                else:
                    break

        if current_car and green_time_available < 0:
            print("A crash happened!")
            print(f"{''.join(current_car)} was hit at {current_car[green_time_available + free_window_duration]}.")
            break
    else:
        car = list(command)
        cars_line.append(car)
