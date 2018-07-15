# def lessThan(x):
#     if x > 5:
#         return x
#     else:
#         return None
# l = [1, 2, 3, 4, 5, 8, 9, 10, 11]
#
# print(list(filter(lessThan, l)))
# letters = dict()
# index = 0
# for i in list(map(chr, range(97, 123))):
#     letters[i] = index
#     index += 1
# print(letters)

# k = [0, 0, 0, 1]
# k = ''.join(str(x) for x in k)
# k = int(k, 2)
# s = 'hello'
# s = s[::-1]
# print(s)
# print(k)


def f(*args):
    print(list(args))


f(10, 20, 30, 50, 80)
f('2/4', '6/4', '4/4')
