fib1 = 0
fib2 = 1

n = 800

i = 1
while(fib1 * fib2 < n):
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    i += 1
    print(fib2, i, fib1 * fib2)
if fib1 * fib2 == n:
    print('True')
else:
    print('False')
