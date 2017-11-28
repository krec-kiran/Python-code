# n=[-3,7,12,0,5,8,4,2,19]

n=[6,1,1,1,1]

count=len(n)

k=2
m=[30,10]

n=sorted(n+m)

print("Sorted Array:",n)
median=int((count+k)/2)

# print(median)

print("The maximum median value to achieve is:",n[median])
