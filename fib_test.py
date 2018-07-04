fib1 = 0
fib2 = 1
fib = []
for i in range(2, 40):
    fib3 = fib1 + fib2
    if fib3 > 4000000:
        break
    if fib3 % 2 == 0:
        fib.append(fib3)
    fib1 = fib2
    fib2 = fib3

print(fib)
print(sum(fib))
# print(list(filter((lambda x: x % 2 == 0), fib)))
# print([x for x in fib if x % 2 == 0])
# Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/
