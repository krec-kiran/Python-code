k = [24, 25, 34, 40, 38, 26, 33, 29, 50, 31, 33, 56, 35, 36, 53, 49, 57, 27, 37, 40,
     48, 44, 32, 35, 45, 52, 43, 47, 26, 51, 55, 28, 41, 42, 46, 51, 25, 30, 44, 54]


def find_dups_miss(arr):
    uniq = set(arr)
    duplicates = sorted(x for x in uniq if arr.count(x) > 1)
    l = list(range(min(uniq), max(uniq) + 1))
    missing = sum(l) - sum(uniq)
    return ([missing, duplicates])


print(find_dups_miss(k))
