# Given three integers a ,b ,c, return the *largest number** obtained after inserting the following operators and brackets*: +, *, ().
test = [5, 6, 2]
sum = 0
from functools import reduce

dummy = [9, -1, 76, 108, 12, -3]
dummy.sort()
print("list sorted in place ", dummy)

if 1 in test:
    test = sorted(test)
    max = max(test)
    if max != 1:
        sum = max * (test[1] + test[0])
    else:
        sum = reduce((lambda x, y: x + y), test)
else:
    sum = reduce((lambda x, y: x * y), test)

print(sum)
