candidates = [21, 17, 96, 71, 76, 62, 48, 42, 55, 75, 55, 98, 9, 88,
              61, 46, 45, 24, 46, 59, 10, 63, 41, 77, 47, 83, 81, 61, 59, 42]


def elections_winners(votes, k):
    total = 0
    big = max(votes)
    for i in votes:
        if i + k > big:
            total += 1
        if k == 0 and i + k == big and votes.count(i) == 1:
            total += 1
    return(total)


print(elections_winners(candidates, 17))
