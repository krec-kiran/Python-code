#  memoize discussion


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib = memoize(fib)

print(fib(10))

x = set(["Perl", "Python", "Java"])
print(x.pop())
print(x)

queue = ['a', 'b', 'c']

queue.append('d')

print(queue)

print(queue.pop(0))

x = [45, 17, 21, -2]

x.sort()

print(x)
