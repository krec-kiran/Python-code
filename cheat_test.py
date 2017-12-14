'''A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?

removNb(26) should return [(15, 21), (21, 15)] '''

import copy
def removNb(n):
  original_elements=[x for x in range(n)]
  original_elements=original_elements[1:]
  toto=sum(range(n+1))
  result=[]
  new_elements=original_elements
  for x in new_elements:
    new_elements.remove(x)
    for y in new_elements:
      if x*y==(toto-(x+y)):
        tup1=(x,y)
        tup2=(y,x)
        result.append(tup1)
        result.append(tup2)
        print(result)
        exit()
    new_elements=copy.deepcopy(original_elements)
  print(result)

removNb(67)
