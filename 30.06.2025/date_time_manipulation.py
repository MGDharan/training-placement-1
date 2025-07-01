# Filename:  date_time_manipulation.py
from datetime import datetime, timedelta
def add_days_to_date(date_str, num_days):
    """Adds a specified number of days to a given date."""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date = date_obj + timedelta(days=num_days)
    return new_date.strftime('%Y-%m-%d')