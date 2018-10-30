def pillars(num_pill, dist, width):
    toto = 0
    if num_pill > 1:
        toto = dist * (num_pill - 1) * 100 + width * (num_pill - 2)
    return toto
