# # # # # from itertools import permutations
# # # # # s="aryan"
# # # # #
# # # # # perms = [''.join(x) for x in permutations(s)]
# # # # #
# # # # # print(perms)
# # # # #
# # # # # s="Hello Worlds!!123"
# # # # # letters=0
# # # # # digits=0
# # # # #
# # # # # for char in s:
# # # # #     if char.isalpha():
# # # # #         letters+=1
# # # # #     elif char.isdigit():
# # # # #         digits+=1
# # # # # print("Letter count:",letters)
# # # # # print("Digit count:",digits)
# # # #
# # # # # values = list()
# # # # # values.append(99)
# # # # # v=[39,-1,10,412,12]
# # # # # values+=v
# # # # # values.sort()
# # # # # print(values)
# # # # #
# # # # # w=(12,-1,13)
# # # # # print(w)
# # # #
# # # # # s = 'Picassocassbentcass'
# # # # # # print(s[2:6],len(s))
# # # # # # s='K' + s[1:]
# # # # # # print(s)
# # # # #
# # # # # # print(s.replace('cass','kent',2))
# # # # #
# # # # # line = 'aaa,bbb,ccccc,dd;ef'
# # # # # print(line.split(';'))
# # # #
# # # # # lineCount = 0
# # # # # with open('bank.py') as file:
# # # # #     for line in file:
# # # # #         lineCount += 1
# # # # #         print(lineCount, line.rstrip())
# # # # # with open('myfile', mode='w') as file:
# # # # #     file.write('Copy and Paste is a design error!')
# # # #
# # # # # **************** Lists *****************
# # # #
# # # # # doubles = [c * 2 for c in 'blah']
# # # # # print(doubles)
# # # # #
# # # # # M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # # # # #
# # # # # # G = [sum(A) for A in M]
# # # # # #
# # # # # # print(G)
# # # # #
# # # # # k = {i: sum(M[i]) for i in range(3)}
# # # # # print(k)
# # # #
# # # # #
# # # # # def countBits(n):
# # # # #     n = bin(n)
# # # # #     n = list(n[2:])
# # # # #     print(n)
# # # # #     b = [x for x in n if x == '0']
# # # # #     print(len(b))
# # # # #
# # # # #
# # # # # countBits(25)
# # # #
# # # # #
# # # # # def findMid(text):
# # # # #     index = int(len(text) / 2)
# # # # #     if len(text) % 2 != 0:
# # # # #         return text[index]
# # # # #     else:
# # # # #         result = text[index - 1] + text[index]
# # # # #         return result
# # # # #
# # # # #
# # # # # text = 'ABCDEFGHIJK'
# # # # # print(findMid(text))
# # # #
# # # # # 0 1 2 3 n = 3 0 1 4 9
# # # #
# # # #
# # # # # def countDigit(n, d):
# # # # #     k = [str(x * x) for x in range(n + 1)]
# # # # #     k = ''.join(k)
# # # # #     print(k)
# # # # #     print("Count is:", (k.count(str(d))))
# # # # #
# # # # #
# # # # # countDigit(3, 4)
# # # #
# # # # #
# # # # # def cubeChecker(volume, side):
# # # # #     if volume <= 0 or side <= 0:
# # # # #         return False
# # # # #     if volume == side**3:
# # # # #         return True
# # # # #     else:
# # # # #         return False
# # # # #
# # # # #
# # # # # print(cubeChecker(343, 6))
# # # #
# # # # #
# # # # # buffet = ('pasta', 'pizza', 'french toast', 'english', 'salads')
# # # # # print("The buffet of resturant X is")
# # # # # for item in buffet:
# # # # #     print(item.title())
# # # # #
# # # # # alien_0 = {'color': 'green', 'points': 5, 'x-pos': 100, 'y-pos': 200}
# # # # # for k, v in alien_0.items():
# # # # #     print(k, ":", v)
# # # # #
# # # # # for v in alien_0:
# # # # #     print(v)
# # # # #
# # # # # import random
# # # # # print(random.randint(1, 100))
# # # # a = 91011121415
# # # # a = str(a)
# # # # # print((a[::-1]))
# # # # # print(''.join(reversed(a)))
# # # # length = len(a)
# # # # count = 1
# # # # # for index in range(0, length - 1):
# # # # #     current = int(a[index + count])
# # # # #     print("Current", a[index], current)
# # # # #     val = current + 1
# # # # #     print(val)
# # # # #     if val % 9 == 0:
# # # # #         count += 1
# # # # #         continue
# # # # #     elif current == val:
# # # # #         current = val
# # # # #         continue
# # # # #     else:
# # # # #         break
# # # # #
# # # # # print(val)
# # # #
# # # # # s = '1011121415'
# # # # # s = '1234578'
# # # #
# # # #
# # # # # def extractor(s, count):
# # # # #     start = 0
# # # # #     end = count
# # # # #     number = list()
# # # # #     while(end <= len(s)):
# # # # #         val = s[start:end]
# # # # #         if int(val) != 0 and int(val) % 9 == 0:
# # # # #             end += 2
# # # # #             start += 1
# # # # #             print("Start:", start, "End:", end)
# # # # #             number.append(val)
# # # # #             continue
# # # # #         number.append(val)
# # # # #         start += count
# # # # #         end += count
# # # # #     return number
# # # # #
# # # # #
# # # # # # s = '599600601602'
# # # # # s = '91011121315'
# # # # # numbers = extractor(s, 1)
# # # # # print(numbers)
# # # # # numbers = list(map(int, numbers))
# # # # # # print(numbers)
# # # #
# # # # # print('{0} Eggs and {1} Apples and {2} Oranges'.format(20, 40, 60))
# # # #
# # # # # l = [12, -1, 4, 6, 100, 13]
# # # # # l.sort()
# # # # # print(l)
# # # # #
# # # # # print(sorted("This is my text written when I was three".split(), key=str.lower))
# # # # #
# # # # # numbers = {4: 'cat', 9: 'mat', -1: 'bat', 200: 'rat'}
# # # # # # print(sorted(numbers.values(), reverse=True))
# # # # # print(sorted(numbers))
# # # # #
# # # # # print([(key, value) for (key, value) in sorted(numbers.items())])
# # # #
# # # # l1 = [10, 15, 20, 30, -1]
# # # # l2 = [10, 20, 80, 90, -1]
# # # # l3 = []
# # # #
# # # # for x in l1:
# # # #     if x in l2:
# # # #         l3.append(x)
# # # # print(l3)
# # # #
# # # #
# # # # def intersect(l1, l2):
# # # #     print([x for x in l1 if x in l2])
# # # #     # print(list(set(l1) & set(l2)))
# # # #
# # # #
# # # # t1 = "WORLD"
# # # # t2 = "WORRY"
# # # #
# # # # t4 = [8, 9, 18]
# # # # t5 = [9, 0, 6, 18, -2]
# # # #
# # # # c1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
# # # # c2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
# # # #
# # # # c3 = [list(filter(lambda x: x not in c1, sublist)) for sublist in c2]
# # # # print(c3)
# # # # c4 = [item for c1 in c2 for item in c1]
# # # # print(c4)
# # # #
# # # # intersect(t4, t5)
# # # #
# # # # #
# # # # # def f(**val):
# # # # #     print(val)
# # # # #
# # # # #
# # # # # f(a=10, b=20)
# # # #
# # # # #
# # # # # def kwargs_function(**kwargs):
# # # # #     for k, v in kwargs.items():
# # # # #         print(k, v)
# # # # #
# # # # #
# # # # # kwargs_function(**{'uno': 'one', 'dos': 'two', 'tres': 'three'})
# # # #
# # # #
# # # # l1 = [12, -1, 90]
# # # # print(min(l1), max(l1))
# # # #
# # # # s = input("Enter a number")
# # # # if (int(s) % 2 == 0):
# # # #     print("Its even!")
# # # # else:
# # # #     print("Its odd!")
# # #
# # # # import math
# # # #
# # # #
# # # # def findGCD(numb1, numb2):
# # # #     gcd = max(list(set(findDivisors(numb1)) & set(findDivisors(numb2))))
# # # #     return gcd
# # # #
# # # #
# # # # def findDivisors(numb1):
# # # #     l1 = []
# # # #     for i in range(1, numb1 + 1):
# # # #         if(numb1 % i == 0):
# # # #             l1.append(i)
# # # #     return l1
# # # #
# # # #
# # # # print(findGCD(45, 54))
# # # #
# # # # print(math.gcd(45, 54))
# # # #
# # # # lcm = int(6 * 8 / findGCD(6, 8))
# # # # print(lcm)
# # # #
# # # # math.pow(2, 3)
# # #
# # # num1 = 12
# # # num2 = 20
# # # l1 = []
# # # l2 = []
# # #
# # # from operator import mul
# # # from functools import reduce
# # # import math
# # #
# # # t1 = []
# # # # for i in range(1, 20):
# # # #     l1.append(num1 * i)
# # # # for i in range(1, 20):
# # # #     l2.append(num2 * i)
# # # # print(min(set(l1) & set(l2)))
# # # # for i in range(2, 100):
# # # #     if num1 % i == 0 and num2 % i == 0:
# # # #         t1.append(i)
# # # #         num1 = int(num1 / i)
# # # #         num2 = int(num2 / i)
# # # #
# # # # product = reduce(mul, t1)
# # # # print(product * num1 * num2)
# # # # math.
# # #
# # #
# # # # def gcd(a, b):
# # # #     """Compute the greatest common divisor of a and b"""
# # # #     while b > 0:
# # # #         a, b = b, a % b
# # # #         print(a, b)
# # # #     return a
# # # #
# # # #
# # # # print(gcd(45, 54))
# # #
# # # [1, 1, 2, 3, 5, 8, 13, 21]
# # # fib1 = 1
# # # fib2 = 1
# # # fib = []
# # # fib.append(fib1)
# # # fib.append(fib2)
# # #
# # # i = 0
# # # count = int(input("Enter number of Fibonaaci numbers required  "))
# # # count -= 2
# # # while i < count:
# # #     fib3 = fib1 + fib2
# # #     fib.append(fib3)
# # #     fib1 = fib2
# # #     fib2 = fib3
# # #     i += 1
# # #
# # # print(fib)
# #
# # # map, filter, reduce: Common Syntax -> (aFunction, aSequence)
# #
# # from functools import reduce
# # k = list(filter((lambda x: x % 2 == 0), [1, 2, 3, 4]))
# # print(k)
# # k = reduce((lambda x, y: x + y), [1, 2, 3, 4])
# # print(k)
# # p = list(map(lambda x: x**2, [1, 2, 3, 4]))
# # print(p)
# #
# # l1 = ['1', '12', '9', '90']
# # print(l1)
# # l1 = list(map(float, l1))
# # print(l1)
#
# # import re
# # pattern = r"CLookie"
# # sequence = "Cookie"
# # if re.match(pattern, sequence):
# #     print("Match!")
# # else:
# #     print("Not a match!")
# # import re
# # print(re.search(r'dog$', 'Cookie cutter Under the dog').group())
#
# # a = 5
# # b = 6
# # print(a, b)
# # a, b = b, a
# # print(a, b)
#
# for i in range(1, 5, 2):
#     print(i)
#
# l1 = [4, 5, 6, 8]
# l2 = [4, 9, 8]
# for i in l1, l2:
#     print("i value is {0}".format(i))
# print([x for x in l1 if x in l2])
# print([x * y for x in l1 for y in l2])
# x = 123.678
# print("%2f" % x)
#
# s = "Hello World Hello Woorld A big line with long sentences"
# print(s.count('o'))
# print(s.split())
#
#
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get(self):
#         print(self.name, self.age)
#
#     def checkStatus(self):
#         if self.age < 18:
#             return "minor"
#         else:
#             return "major"
#
#
# s = Student("Kiran", 16)
# s.get()
# print(s.checkStatus())
#
#
# print([x for x in range(10) if x % 2 == 0])
# x = list(filter((lambda x: x % 2 == 0), [1, 2, 3, 4, 5,
#                                          6, 7, 8, 9, 12, 14, 15, 17, 19, 23]))
#
# x = list(filter((lambda x: x % 3 == 0), [1, 2, 3, 4, 5,
#                                          6, 7, 8, 9, 12, 14, 15, 17, 19, 23]))
# print(x)
#
# min = (lambda x, y: x if x < y else y)
#
# print(min(10, 20))
#
# l1 = [1, 2, 3, 3, 4, 5]
# l2 = [3, 4, 5]
#
# print(l1 + l2)
#
# print(list(set(l1) & set(l2)))
#
# print(set(l1))
#
#

# alien_0 = {'color': 'green', 'points': 5, 'x-pos': 100, 'y-pos': 200}
# for k, v in alien_0.items():
#     print(k, ":", v)
#
# print(alien_0.values())


# while True:
#     try:
#         a = int(input("Enter integer"))
#         a += 1
#         print(a)
#         break
#     except ValueError:
#         print("Pls make sure to use integer")
#     except:
#         break
#     finally:
#         print("Final block")

# d = {1: 'a', 2: 'b', 3: 'c'}
# for k in d:
#     print(d[k])
#
# color_list = ["Red", "Green", "White", "Black"]
# print(color_list[:-1])

# def greet(name):
#     print("Hello " + name)
#
#
# greet("Kiran")
#
# import dis
# dis.dis(greet)

# import datetime
#
# print(datetime.datetime.today().strftime("%w"))


# from functools import reduce
# from operator import mul
# l1 = [2, 3, 4]
#
# print(reduce(mul, l1))

# import collections
#
# c = collections.Counter('Hello World')
# print(c)
# print("Most Common", c.most_common(3))

# a = 36
# b = 60
#
# # while b > 0:
# #     a, b = b, a % b
# # print(a)
# while b > 0:
#     a, b = b, a % b
# print(a)

t = [(1, 'd'), (2, 'c'), (3, 'b'), (4, 'a')]

print(sorted(t, key=lambda x: x[1]))
