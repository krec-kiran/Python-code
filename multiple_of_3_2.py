from itertools import permutations

1234


def find_mult_3(num):
    num = str(num)
    values = [list(num)]
    for i in range(2, len(num) + 1):
        l = list(permutations(num, i))
        values.append([''.join(x) for x in l])

    result = [int(x) for k in values for x in k if int(x) % 3 == 0]

    if 0 in result:
        result.remove(0)

    result = set(result)

    return([len(result), max(result)])


print(find_mult_3(7766553322))
print(find_mult_3(6630))
