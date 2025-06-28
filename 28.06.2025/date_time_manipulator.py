# Filename:  date_time_manipulator.py
import datetime

def days_until_christmas():
    today = datetime.date.today()
    christmas = datetime.date(today.year, 12, 25)
    if today > christmas:
        christmas = datetime.date(today.year + 1, 12, 25)
    return (christmas - today).days

def format_date(date_obj, format_string="%Y-%m-%d"):
    return date_obj.strftime(format_string)