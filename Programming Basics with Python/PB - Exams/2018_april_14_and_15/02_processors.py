planned_processors_num = int(input())
workers_num = int(input())
work_days = int(input())

possible_work_time = workers_num * 8 * work_days
processors_num = possible_work_time // 3

planned_earnings = planned_processors_num * 110.10
earnings = processors_num * 110.10

money_diff = abs(planned_earnings - earnings)

if earnings > planned_earnings:
    print(f"Profit: -> {money_diff:.2f} BGN")
elif earnings < planned_earnings:
    print(f"Losses: -> {money_diff:.2f} BGN")
