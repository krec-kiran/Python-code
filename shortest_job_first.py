def SJF(jobs, index):
    total = 0
    i = -1
    while jobs[index] > 0:
        if i < len(jobs) - 1:
            i += 1
        else:
            i = 0

        l = [x for x in jobs if x != 0]
        shortest = jobs.index(min(l))
        total += min(l)
        jobs[shortest] = 0

    return(total)


print(SJF([3, 10, 20, 1, 2], 0))
