'''Chef is a well known programmer. He owns a brand new Android phone of screen size of dimension n × m (n denotes the height of the phone and m denotes the width).
 Chef wants to design a program for painting the screen. He figured out c colors, which he will use to paint the screen.
 He wants to paint some rectangular section of pixels of the screen each with different color.
 Also Chef would like to use all of his c colors in painting.

Can you help Chef in finding number of different dimensions of rectangular section he can paint?
In other words, find number of pairs x, y such that Chef can paint a rectangular section of
dimension x × y (x denotes height, y denotes width) on the screen.
Please note that Chef uses a fix orientation of his phone and is not allowed to rotate it, i.e.
height always stays n and width always stays m and not the other way around.'''

def problem(n):
    return [x for x in range(1, n + 1) if n % x == 0]

colors = 12

print(problem(colors))

n = problem(colors)

w = 4
h = 6

m = [(x, y) for x in n for y in n if x * y == colors]
print(m)

print("Possible colors for chef...")

for item in m:
    if item[0] <= w and item[1] <= h:
        print(item)
