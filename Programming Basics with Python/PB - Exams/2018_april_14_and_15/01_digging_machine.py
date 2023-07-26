from math import ceil

gpu_price = int(input())
transistor_price = int(input())
electricity_per_gpu_price = float(input())
gpu_earnings_daily = float(input())

gpus = 13 * gpu_price
transistors = 13 * transistor_price
other_parts = 1000
total_prices = gpus + transistors + other_parts

gpus_earnings = (gpu_earnings_daily - electricity_per_gpu_price) * 13
return_time = ceil(total_prices / gpus_earnings)

print(total_prices)
print(return_time)
