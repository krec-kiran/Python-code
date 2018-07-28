def projectPartners(n):
    length = n - 1
    count = 0
    for i in range(n):
        count += length
        length -= 1
    return count
