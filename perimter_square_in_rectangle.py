def perimeter(n):
    fib1 = 1
    fib2 = 1
    total = 2
    for i in range(n - 1):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        total += fib3
    return(total * 4)


print(perimeter(5))
