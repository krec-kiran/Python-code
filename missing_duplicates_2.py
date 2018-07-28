def find_dups_miss(arr):
    seen = set()
    dupes = []

    for i, doi in enumerate(arr):
        if doi not in seen:
            seen.add(doi)
        else:
            dupes.append(doi)

    l = list(range(min(seen), max(seen) + 1))
    missing = set(l) - set(seen)
    return ([missing.pop(), sorted(dupes)])


k = [24, 25, 34, 40, 38, 26, 33, 29, 50, 31, 33, 56, 35, 36, 53, 49, 57, 27, 37, 40,
     48, 44, 32, 35, 45, 52, 43, 47, 26, 51, 55, 28, 41, 42, 46, 51, 25, 30, 44, 54]

print(find_dups_miss(k))
