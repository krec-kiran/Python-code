def queue(q, i):
    tickets = q[i]
    time = 0
    while tickets > 1:
        q[:] = [x - 1 for x in q]
        length = sum([1 for x in q if x >= 0])
        time += length
        tickets -= 1
    k = [x for x in q[:i + 1] if x > 0]
    ahead = len(k)
    time += ahead
    return(time)
