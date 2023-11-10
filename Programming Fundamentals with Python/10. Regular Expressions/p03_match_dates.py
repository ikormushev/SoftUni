import re

dates = input()

dates_pattern = r"\b(?P<day>\d{2})(?P<separator>\.|-|/)(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"
valid_dates = re.finditer(dates_pattern, dates)

for date in valid_dates:
    date_info = date.groupdict()
    day = date_info["day"]
    month = date_info["month"]
    year = date_info["year"]
    print(f"Day: {day}, Month: {month}, Year: {year}")
