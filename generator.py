def fibonacci():
    """Fibonacci numbers generator, first n"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

counter = 0
for x in f:
    print(x)
    counter += 1
    if (counter > 20):
        break
