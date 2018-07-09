import math


def ellipse(a, b):
    area = math.pi * a * b
    perimeter = math.pi * (3 / 2 * (a + b) - math.sqrt(a * b))
    message = ("Area: %.1f, perimeter: %.1f" % (area, perimeter))
    return(message)


print(ellipse(5, 2))
