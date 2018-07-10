from __future__ import division

n = '0.142857142857142857'
n = 69
val = float(69)

cycle = ''

for i in range(2, n + 1):
    if n % i == 0 and 10 % i == 0:
        print(-1)
        exit()
n = 1 / val
k = ("%.30f" % n)
print("K is", k)
n = str(n)
print("String", n)
print("Extract", n[2:])
for x in k[2:]:
    if x not in cycle:
        cycle += x
    else:
        break
print("Cycle", cycle)
print(len(cycle))
