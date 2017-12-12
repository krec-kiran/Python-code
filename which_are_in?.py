a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

out=["arp", "live", "strong"]

result=[]

for x in a1:
  for y in a2:
    if x in y:
      result.append(x)

k=list(set(result))
k.sort()
print(k)




