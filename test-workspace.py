# num=10

# num+=50

# num+=1
# print(num)

def sqrt(x):
  return x*x

strings = ["hello", "kiran", "TN126BJ"]

numbers = [1,2,3,4]

items = [2,3,5,0.8,"abc",'a','e','i']

# print(''.join(numbers))

print(''.join(map(str,items)))

print(','.join(strings) )


# Map takes a funcation and applies that to all members of collection
# good reference - http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php
# the function could also be replaced by lambda

print(list(map(sqrt,numbers)))

print(list(map((lambda x:x**3),numbers)))
