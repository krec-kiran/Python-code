import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a, b, c):
        self.a = Point(a)
        self.b = Point(b)
        self.c = Point(c)

    def findDistance(self):
        print(self.a.x.x)
        val = math.sqrt((pow((self.a.x.x - self.b.x.x), 2) -
                         pow((self.a.x.y - self.b.x.y), 2)))
        print('val', val)

        #
        #
        # class Triangle:
        #     def self(Point(x1,))
        #
        #
        # def Triangle(a1=Point(10, 20), b1=Point(40, 10), c1=Point(10, 50)):
        #     print(a1, b1, c1)
        #     return (a1, b1, c1)
        #

#
# p = Point(10, 20)
# print(p.x, p.y)


k = Triangle(Point(10, 10), Point(40, 10), Point(40, 50))

print(k.a.x.y)
k.findDistance()

print(k.b.x.x)

# def triangle_perimeter(Triangle(Point(10, 10), Point(40, 10), Point(10, 50)):
