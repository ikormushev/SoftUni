deposit = float(input())
months = int(input())
annual_interest_rate_in_percent = float(input()) / 100

interest_per_year = deposit * annual_interest_rate_in_percent
interest_per_month = interest_per_year / 12

final_sum = deposit + (months * interest_per_month)

print(final_sum)