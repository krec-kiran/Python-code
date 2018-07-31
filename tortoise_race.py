def race(v1, v2, g):
    if v1 > v2:
        return
    t = int(g * 60 * 60 / (v2 - v1))
    time = [0] * 3
    if t >= 3600:
        hrs = int(t / (60 * 60))
        time[0] = hrs
        t = t - (60 * 60 * hrs)
    if t > 60:
        mins = int(t / 60)
        time[1] = mins
        secs = t % 60
        time[2] = secs

    return time


print(race(720, 850, 70))
