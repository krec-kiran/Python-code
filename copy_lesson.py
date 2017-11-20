from copy import deepcopy

lst1 = ['a','b',['ab','ba']]

lst2 = deepcopy(lst1)

tp = (10,20,30)

tp2 = (40,89)

print(tp+tp2)
print(lst1)

for x in tp:
  print(x)


print(lst2)

print(lst2)
print(lst1)

lst = ['C']*3

print(''.join(lst))


def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)

value = f('a')

print(value)




