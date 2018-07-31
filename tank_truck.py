# check the math here to understand the formula used here - https://www.mathopenref.com/cylindervolpartial.html

import math


def tankvol(h, d, vt):
    r = d / 2
    denominator = math.pi * r * r
    length = vt / denominator
    area = r * r * math.acos((r - h) / r) - (r - h) * \
        math.sqrt(2 * r * h - h * h)

    volume = area * length

    return(int(volume))


print(tankvol(40, 120, 3500))
print(tankvol(60, 120, 3500))
print(tankvol(80, 120, 3500))
