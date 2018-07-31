def get_score(n):
    total = 0
    for i in range(n):
        total += n * 50
        n = n - 1
    return total


print(get_score(3))
print(get_score(5))
print(get_score(7))
