pool_volume_lt = int(input())
first_pipe_lt_per_hr = int(input())
second_pipe_lt_per_hr = int(input())
hours_missing = float(input())

first_pipe_pumped_water = first_pipe_lt_per_hr * hours_missing
second_pipe_pumped_water = second_pipe_lt_per_hr * hours_missing
water_sum = first_pipe_pumped_water + second_pipe_pumped_water

pool_water_percent_full = (water_sum / pool_volume_lt) * 100
first_pipe_water_percent = (first_pipe_pumped_water / water_sum) * 100
second_pipe_water_percent = (second_pipe_pumped_water / water_sum) * 100

if water_sum > pool_volume_lt:
    water_overflow = water_sum - pool_volume_lt
    print(f"For {hours_missing} the pool overflows with {water_overflow} liters.")
else:
    print(f"The pool is {pool_water_percent_full:.2f}% full. Pipe 1: {first_pipe_water_percent:.2f}%."
          f"Pipe 2: {second_pipe_water_percent:.2f}%.")
