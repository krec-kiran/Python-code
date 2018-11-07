array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
k = 0


def diagonal_sum(array):
    sum = 0
    k = 0
    for i in array:
        sum += i[k]
        k += 1
    return sum


print(diagonal_sum(array))
