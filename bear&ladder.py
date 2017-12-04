'''Bearland has infinitely many cities, numbered starting from 1.
Some pairs of cities are connected with bidirectional roads:

There are roads 1-2, 3-4, 5-6, 7-8, and so on (there is a road between cities 2*i+1 and 2*i+2
for every non-negative integer i).
There are roads 1-3, 3-5, 5-7, 7-9, ... (between every two consecutive odd numbers).
There are roads 2-4, 4-6, 6-8, 8-10, ... (between every two consecutive even numbers).
This is how the first few cities and roads between them look like:

You are given Q queries. In each query, for the given pair of different cities a and b,
you should check if there is a road between them. For each query, print "YES" or "NO" accordingly.'''

# roads=[17,2384823]
# roads=[10,12]
# roads=[1,4]
roads=[999999999,1000000000]
minimum=min(roads)
maximum=max(roads)

check1 = minimum + 1
check2 = minimum + 2

if (check1==maximum or check2==maximum ):
  print("YES")
else:
  print("NO")

# rules = [check1,check2]
# if all(rules):
#   print("YES")
# else:
#   print("NO")
