from math import floor

centuries = int(input())

years = centuries * 100
days = floor(years * 365.2422)  # could be also done with int()
hours = days * 24
minutes = hours * 60

print(f"{centuries:.0f} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")
