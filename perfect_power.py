import math
def isPP(n):
  for i in range(2,n):
    if n%i==0:
      for k in range(int(math.log(n,2))+1):
        if pow(i,k)==n:
          return [i,k]

  return None



print(isPP(16))
print(isPP(25))
print(isPP(343))



