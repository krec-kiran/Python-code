arr = [1, 1, 1, 2, 1, 1]
arr = [3, 10, 3, 3, 3]
arr = [0, 0, 0.55, 0, 0]


def find_uniq(arr):
    k = sorted(arr)
    if k[len(k) - 1] != k[0] and k[len(k) - 1] != k[1]:
        return(k[len(k) - 1])
    else:
        return(k[0])


print(find_uniq(arr))
