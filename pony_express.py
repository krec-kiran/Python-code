def riders(stations):
    distance = 0
    riders = 1
    for i in range(len(stations) - 1):
        distance += stations[i]
        if distance + stations[i + 1] > 100:
            riders += 1
            distance = 0
    return riders
