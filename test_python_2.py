# # def factorial(n):
# #     if n == 0:
# #         return 0
# #     if n == 1:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)
# #
# #
# # print(factorial(5))
# #
# #
# # lst = [2, 4, 6, 8, 10]
# # print(list(map(factorial, lst)))
#
# from math import sqrt
#
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(sqrt(n)) + 1):
#         if (n % i) == 0:
#             return False
#     return True
#
#
# def prime_generator(n):
#     primes = []
#     for i in range(n + 1):
#         if is_prime(i):
#             primes.append(i)
#     return primes
#
#
# print(prime_generator(31))

lst = [1, 4, 45, 6, 10, -8]


def sum_pair(lst, target):
    for num_1 in sorted(lst):
        num_2 = target - num_1
        if num_2 in lst:
            return (num_1, num_2)
    return []


print(sum_pair(lst, 37))
