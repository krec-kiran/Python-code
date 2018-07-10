# creating two dimensional array - use list comprehension

s = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
tv = [[0 for i in range(8)] for j in range(5)]

k = 0
for i in range(5):
    for j in range(8):
        tv[i][j] = s[k]
        k += 1

print(tv)
