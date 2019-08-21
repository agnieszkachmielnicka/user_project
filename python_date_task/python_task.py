import sys
import datetime

with open(sys.argv[1], 'r') as date_file:
    numbers = date_file.read().split('/')


new_numbers = list(map(int, numbers))


def days_in_month(date_to_check):
    next_month = date_to_check.replace(day=28) + datetime.timedelta(days=4)
    result_date = next_month - datetime.timedelta(days=next_month.day)
    return int(result_date.day)


def get_year():
    maximum = max(new_numbers)
    minimum = min(new_numbers)
    if maximum >= 2000:
        year = maximum
        new_numbers.remove(maximum)
    else:
        year = minimum + 2000
        new_numbers.remove(minimum)
    if year:
        return year
    return ""


def get_month():
    month = min(new_numbers)
    if month > 12 or month == 0:
        return ""
    return month


def get_day():
    day = max(new_numbers)
    if day > days_in_month(datetime.date(year, month, 1)) or day == 0:
        return ""
    return day


year = get_year()
month = get_month()
day = get_day()

if not year or not month or not day:
    result = "is illegal"
else:
    result = "{}-{:02d}-{:02d}".format(year, month, day)
print(result)
