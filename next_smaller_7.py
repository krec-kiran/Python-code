from itertools import permutations


def next_smaller(n):
    s = list(map(int, list(str(n))))
    print(s)
    l = [2:]


print(next_smaller(531))
print(next_smaller(1234567908))
