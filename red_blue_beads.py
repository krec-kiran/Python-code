def count_red_beads(N_blue):
    if N_blue != 0:
        return (N_blue - 1) * 2
    else:
        return 0


print(count_red_beads(3))
print(count_red_beads(1))
print(count_red_beads(5))
