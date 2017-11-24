# num=10

# num+=50

# num+=1
# # print(num)

# def sqrt(x):
#   return x*x

# strings = ["hello", "kiran", "TN126BJ"]

# numbers = [1,2,3,4]

# items = [2,3,5,0.8,"abc",'a','e','i']

# # print(''.join(numbers))

# print(''.join(map(str,items)))

# print(','.join(strings) )


# # Map takes a funcation and applies that to all members of collection
# # good reference - http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php
# # the function could also be replaced by lambda

# print(list(map(sqrt,numbers)))

# print(list(map((lambda x:x**3),numbers)))


# Sort based on the user provided constraint in key - by length or value
# of second element as the following

# take second element for sort
# def takeSecond(elem):
#     print(elem)
#     return elem[1]

# # random list
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# # print(takeSecond((3, 4)))

# # sort list with key
# sortedList = sorted(random, key=takeSecond)

# testlist = sorted(random)

# print(testlist)
# # print list
# print('Sorted list:', sortedList)


# Enumerate example - useful for indexed series - 0,1,2...

# L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for i, v in enumerate(L):
#     if i % 3 == 0:
#         print(i,v)

# for i in L:
#     if i % 2 == 0:
#         print(i)

# Merging two sorted lists

# a=[1,3,5,7]
# b=[2,4,6,8]
# c=[]

# # a.extend(b)
# # c=sorted(a)
# # print(c)

# # difference between append and extend - append adds in a list while extends adds in all elements into the source list

# a.append(b)
# print(a)


# while a and b:
#   if a[0] < b[0]:
#     c.append(a.pop(0))
#   else:
#     c.append(b.pop(0))

# print(c)

# use str() to convert digits to string format before using join or other functions

# print(''.join(str(x) for x in range(10)))

# import os

# print(os.path.expanduser('~'))

# print(os.getcwd())

# import itertools

# print([x for x in itertools.combinations('125',2)])

# print((x ** 3 for x in range(5)))

# expression type generator - list comprehension
# gen = (x ** 3 for x in range(5))

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def test(arg):
#   """test function returns an argument"""
#   return arg

# print(test(10))
# print(test.__doc__)

# keyword arguments - name=value kwargs
# *args - arbitrary number of arguments of any length

# def kwargs(**kwargs):
#   for k,v in kwargs.items():
#     print(k,v)

# kwargs(**{'uno':'one','dos':'two','tres':'three'})

# kwargs(dos='two', tres='three', uno='one')

# L = [1,5,6,6,8,6,9]

# L.remove(6)

# print(L)

# s="hello"

# print(list(map(s.count,s)))

# a = [[1,2,3,4],[9,5,6,7]]

# b = [item for x in a for item in x]
# c = [item*2 for x in a for item in x]
# print(b)
# print(c)

a=[1,2,3]
b=[4,5,6]
z=list(zip(a,b))
print(z)
c,d=zip(*z)
print("Before zip",a,b)
print("Recovered after zip",list(c),list(d))

keys=['a','b','c']
values = [1,2,3]

d3=dict(zip(keys,values))

print("Dict using zip",d3)

d2={}

for k,v in zip(keys,values):
  d2[k]=v

print(d2)

# dictionary comprehension example

d4 = {k:v for k,v in zip(keys,values)}
print(d4)

D = dict.fromkeys('Hello')
print(D)


class Point():
  def __init__(self,x,y):
          self.x=x
          self.y=y
  def __repr__(self):
   return 'Point(x=%s, y=%s)' % (self.x, self.y)


p=Point(12,13)
print(p)
