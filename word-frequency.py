ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""

words=ss.split()

# print(words)

# d={}.fromkeys(words,0)

# print(d)

# for word in words:
#   d[word]+=1;

# print(d)

# from collections import defaultdict
# d = defaultdict(int)

# print(d)

# for w in words:
#   d[w]+=1

# print(d)

# three ways of dictionary - 1. d={}, d={}.fromkeys(words,0),defaultdict(int) - good for counting as they initialise

# initialising dictionary with list as values - example - 1

# dictionary with values as list members -{ US :[SFO,LA] } etc

# cities = {'San Francisco': 'US', 'London':'UK',
#         'Manchester':'UK', 'Paris':'France',
#         'Los Angeles':'US', 'Seoul':'Korea'}

# from collections import defaultdict
# dl = defaultdict(list)

# for k,v in cities.items():
#   dl[v].append(k)

# print(dl)

# initialising dictionary with list as values - example - 2

# dictionary with number of digits as key and numbers themselves as values
# L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]


# # expected output - {1: [1, 2, 4, 8], 2: [16, 32, 64], 3: [128, 256, 512], 4: [1024], 5: [32768, 65536], 10: [4294967296]})

# from collections import defaultdict
# dl = defaultdict(list)

# # to find length of digits use str to convert to string then calculate length like len(str(val))
# for v in L:
#     dl[len(str(v))].append(v)

# print(dl)

# print({k:v for k,v in dl.items()})

# Map with lambda and sequence of functions

def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]

for r in range(5):
    value = list(map(lambda x:x(r),funcs))
    print(value)

def add(a,b,c):
    return (a+b+c)

# Map with multiple sequence of arguments example

print(list(map(add,[2,3,4],[3,4,5],[2,2,2])))

# zip_longest() makes an iterable by aggregating elements from two iterables

m = [1,2,3]
n = [1,4,9,4]
q = [5,6,7]
from itertools import zip_longest

for i,j,k in zip_longest(m,n,q):
  print(i,j,k)
