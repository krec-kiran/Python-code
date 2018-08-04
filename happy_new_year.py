# def next_happy_year(year):
#     year += 1
#     while(len(set(str(year))) != len(str(year))):
#         year += 1
#     return year
#
#
# print(next_happy_year(1123))
# print(next_happy_year(2001))
# print(next_happy_year(2334))

# from datetime import date
from datetime import date
import datetime
a = date(2018, 8, 21)
print(a)
for i in range(5):
    a += datetime.timedelta(days=10)
    print(a)
