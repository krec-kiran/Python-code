import calendar
from datetime import date
import datetime


def date_nb_days(deposit, target, p):
    perDay = p / 36000
    count = 0
    a = date(2016, 1, 1)
    while(deposit < target):
        deposit = deposit + (perDay * deposit)
        count += 1
    a += datetime.timedelta(days=count)
    target_date = "{}-{}-{}".format(
        str(a.year), str(a.month) if a.month > 9 else str(0) +
        str(a.month), str(a.day) if a.day > 9 else str(0) + str(a.day))
    return(target_date)


print(date_nb_days(5000, 15000, 2))
