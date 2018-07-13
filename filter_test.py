# def lessThan(x):
#     if x > 5:
#         return x
#     else:
#         return None
# l = [1, 2, 3, 4, 5, 8, 9, 10, 11]
#
# print(list(filter(lessThan, l)))
letters = dict()
index = 0
for i in list(map(chr, range(97, 123))):
    letters[i] = index
    index += 1
print(letters)
