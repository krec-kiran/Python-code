# Solutions works only n being prime!

n = 17
d = 10

l = []
r = 0
while(n - r) != 1:
    r = d % n
    val = int(d / n)
    d = r * 10
    l.append(val)
print(l)
post = []
for i in l:
    k = 9 - i
    post.append(k)
print("Final", l + post)
print("reccurring cycle", len(l + post))
