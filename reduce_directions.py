k = ["NORTH", "WEST", "SOUTH", "EAST"]
p = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]


def dirReduc(k):
    i = 0
    while i < len(k) - 1:
        if k[i] == 'NORTH' and k[i + 1] == 'SOUTH':
            k.pop(i)
            k.pop(i)
            i = 0
        elif k[i] == 'SOUTH' and k[i + 1] == 'NORTH':
            k.pop(i)
            k.pop(i)
            i = 0
        elif k[i] == 'EAST' and k[i + 1] == 'WEST':
            k.pop(i)
            k.pop(i)
            i = 0
        elif k[i] == 'WEST' and k[i + 1] == 'EAST':
            k.pop(i)
            k.pop(i)
            i = 0
        else:
            i += 1
    return(k)


print(dirReduc(k))
print(dirReduc(p))
