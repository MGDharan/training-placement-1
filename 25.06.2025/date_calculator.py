# Filename:  date_calculator.py
from datetime import datetime, timedelta

def days_between(date1_str, date2_str, format="%Y-%m-%d"):
    date1 = datetime.strptime(date1_str, format)
    date2 = datetime.strptime(date2_str, format)
    diff = date2 - date1
    return abs(diff.days)

date1 = "2024-03-15"
date2 = "2024-04-20"
days = days_between(date1, date2)
print(f"Number of days between {date1} and {date2}: {days}")