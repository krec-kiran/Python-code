# isPP(4) => [2,2]
# isPP(9) => [3,2]
# isPP(5) => None

# pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]

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



