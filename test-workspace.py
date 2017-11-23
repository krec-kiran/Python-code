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
def takeSecond(elem):
    print(elem)
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# print(takeSecond((3, 4)))

# sort list with key
sortedList = sorted(random, key=takeSecond)

testlist = sorted(random)

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
