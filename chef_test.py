# n=[-3,7,12,0,5,8,4,2,19]



n=[6,1,1,1,1,2,4,9]

count=len(n)

k=5
m=[30,10,0,11,19]

n=sorted(n+m)

print("Sorted Array:",n)
median=int((count+k)/2)

# print(median)

print("The maximum median value to achieve is:",n[median])



# for x in n:
#   for y in n:
#     if (x*y)==12:
#       print(x,y)
