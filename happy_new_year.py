def next_happy_year(year):
    year += 1
    while(len(set(str(year))) != len(str(year))):
        year += 1
    return year


print(next_happy_year(1123))
print(next_happy_year(2001))
print(next_happy_year(2334))
