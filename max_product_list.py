l = [10, 8, 3, 2, 1, 4, 10]
n = 5
l = sorted(l, reverse=True)
print(l)
product = 1
for i in range(n):
    product *= l[i]
print(product)
