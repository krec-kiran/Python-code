def distribute(candies, children):
    if children <= 0:
        return []
    l = [0] * children
    while candies > 0:
        for i in range(children):
            if candies > 0:
                l[i] += 1
                candies -= 1
    return(l)


print(distribute(15, 10))
