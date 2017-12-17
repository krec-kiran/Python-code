from itertools import *

def find_mult_3(num):
  result=[]
  div3=[]
  for i in range(1,len(num)+1):
   result.extend(list((map("".join,permutations(num,i)))))
   map(int,result)
   result = [s.lstrip("0") for s in result]
   result=list(filter(None,result))
   result=list(set(result))

  for k in result:
    if int(k)%3==0:
      div3.append((int(k)))
  return [len(div3),max(div3)]


print(find_mult_3('302'))
