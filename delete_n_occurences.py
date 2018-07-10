k = [1, 2, 3, 1, 2, 1, 2, 3]
n = 2

result = list()

for x in k:
    if result.count(x) < n:
        result.append(x)
print(result)
