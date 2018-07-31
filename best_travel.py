from itertools import permutations
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64,
      123, 2333, 144, 50, 132, 123, 34, 89]

towns = list(permutations(xs, 3))
towns = [sum(x) for x in towns if sum(x) <= 230]
print(towns)
# print(max(towns))
big = max(towns)

if big:
    print(big)
else:
    print('None')
