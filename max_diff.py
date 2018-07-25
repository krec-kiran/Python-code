numbers = [13, 10, 2, 9, 5, 13, 17, 19, 5, 2, 2, 12, 89, 12, 12, 17]
print(numbers)

numbers = list(map(str, numbers))
# numbers = str(numbers)

# numbers = sorted(numbers)


d = dict()

k = 0
for i in range(len(numbers)):
    freq = numbers.count(numbers[i])
    if freq not in d.keys():
        d[freq] = [int(numbers[i])]
    elif int(numbers[i]) not in [p for x in d.values() for p in x]:
        d[freq].append(int(numbers[i]))
    k += 1

print(d)

n = 17
for k, v in d.items():
    if n in v:
        print(k)
