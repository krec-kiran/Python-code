n = '0.142857142857142857'

cycle = ''

for x in n:
    if x not in cycle:
        cycle += x
        print(cycle)
