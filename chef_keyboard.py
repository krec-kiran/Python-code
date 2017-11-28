def problem(n):
  return [x for x in range(1,n+1) if n%x==0]

colors=24

print(problem(colors))

n=problem(colors)

w=5
h=10

m=[(x,y) for x in n for y in n if x*y==colors]
print(m)

print("Possible colors for chef...")

for item in m:
  if item[0] <= w and item[1]<= h:
    print(item)
