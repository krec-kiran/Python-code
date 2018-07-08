a = ['XOOXO',
     'XOOXO',
     'OOOXO',
     'XXOXO',
     'OOOOO']

p = 0
q = 0
area = 0
for p in range(5):
    for q in range(5):
        if (a[p][q] == 'X') and p + 1 < 5:
            if a[p + 1][q] == 'X' or a[p][q + 1] == 'X':
                area += 2
            area += 2
            print("current-area:", p, q, area)
print(area)
