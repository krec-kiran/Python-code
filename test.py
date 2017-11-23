# # zip is to aggregates two lists and returns an iterator

# numberList = [1, 2, 3,4,5]
# strList = ['one', 'two', 'three']

# # No iterables are passed
# result = zip()

# print(list(zip(numberList)))

# # Converting itertor to list
# resultList = list(result)
# print(resultList)

# # Two iterables are passed
# result = zip(numberList, strList)

# # Converting itertor to set
# resultSet = set(result)
# print(resultSet)

a = [1,2,3,5,7,9,7]
b = [2,3,5,6,7,8,7]
print(list(filter(lambda x:x in a,b)))

print((set(a) & set(b)))

# reduce example
from functools import reduce

f=lambda a,b:a if(a>b) else b


x = reduce(f,[47,11,42,102,13])
print(x)

f2=lambda a,b:a+b

y=reduce(f2,[47,11,42,102,13])
print(y)


fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x:x%3==0,fib)
print(list(result))
