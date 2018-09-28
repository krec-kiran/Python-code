from datetime import date
k = date(2002, 12, 4).weekday()
print(k)

year = 2018
month = 1
while month < 13:
    for i in range(1, 32):
        k = date(year, month, i)
        if k == 4:
            count += 1
    month += 1

print("unlucky days", k)
